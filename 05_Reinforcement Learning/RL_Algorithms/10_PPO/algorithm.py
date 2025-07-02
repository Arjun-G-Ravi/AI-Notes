import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.distributions import Categorical

class ActorCritic(nn.Module):
    def __init__(self, state_dim, action_dim):
        super(ActorCritic, self).__init__()
        
        # Shared network layers
        self.shared = nn.Sequential(
            nn.Linear(state_dim, 64),
            nn.ReLU()
        )
        
        # Actor (policy) network
        self.actor = nn.Sequential(
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, action_dim),
            nn.Softmax(dim=-1)
        )
        
        # Critic (value) network
        self.critic = nn.Sequential(
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 1)
        )
        
    def forward(self):
        raise NotImplementedError
    
    def act(self, state):
        shared_features = self.shared(state)
        action_probs = self.actor(shared_features)
        dist = Categorical(action_probs)
        action = dist.sample()
        action_log_prob = dist.log_prob(action)
        
        return action.item(), action_log_prob.cpu().item()  # Convert to CPU and get value
    
    def evaluate(self, state, action):
        shared_features = self.shared(state)
        action_probs = self.actor(shared_features)
        dist = Categorical(action_probs)
        
        action_log_probs = dist.log_prob(action)
        dist_entropy = dist.entropy()
        
        state_values = self.critic(shared_features)
        
        return action_log_probs, state_values, dist_entropy

class PPO:
    def __init__(self, state_dim, action_dim, lr=3e-5, gamma=0.99, eps_clip=0.2, K_epochs=10, gae_lambda=0.95, device='cpu'):
        self.gamma = gamma
        self.eps_clip = eps_clip
        self.K_epochs = K_epochs
        self.gae_lambda = gae_lambda
        self.device = device
        
        self.policy = ActorCritic(state_dim, action_dim).to(self.device)
        self.optimizer = optim.Adam(self.policy.parameters(), lr=lr)
        
        self.policy_old = ActorCritic(state_dim, action_dim).to(self.device)
        self.policy_old.load_state_dict(self.policy.state_dict())
        
        self.MseLoss = nn.MSELoss()
    
    def select_action(self, state):
        with torch.no_grad():
            state = torch.FloatTensor(state).to(self.device)
            action, action_log_prob = self.policy_old.act(state)
        
        return action, action_log_prob
    
    def update(self, memory):
        # Monte Carlo estimate of rewards
        rewards = []
        discounted_reward = 0
        for reward, is_terminal in zip(reversed(memory.rewards), reversed(memory.is_terminals)):
            if is_terminal:
                discounted_reward = 0
            discounted_reward = reward + (self.gamma * discounted_reward)
            rewards.insert(0, discounted_reward)
        
        # Normalize the rewards
        rewards = torch.tensor(rewards, dtype=torch.float32).to(self.device)
        rewards = (rewards - rewards.mean()) / (rewards.std() + 1e-8)
        
        # Convert list to tensor
        old_states = torch.tensor(np.array(memory.states), dtype=torch.float32).to(self.device)
        old_actions = torch.tensor(np.array(memory.actions), dtype=torch.int64).to(self.device)
        old_log_probs = torch.tensor(np.array(memory.log_probs), dtype=torch.float32).to(self.device)
        
        # Calculate advantages using GAE
        advantages = []
        gae = 0
        with torch.no_grad():
            values = self.policy_old.evaluate(old_states, old_actions)[1].squeeze()
            next_value = 0  # For last state
            
            for i in reversed(range(len(memory.rewards))):
                if memory.is_terminals[i]:
                    next_value = 0
                
                delta = memory.rewards[i] + self.gamma * next_value * (1 - memory.is_terminals[i]) - values[i]
                gae = delta + self.gamma * self.gae_lambda * (1 - memory.is_terminals[i]) * gae
                advantages.insert(0, gae)
                next_value = values[i]
        
        advantages = torch.tensor(advantages, dtype=torch.float32).to(self.device)
        advantages = (advantages - advantages.mean()) / (advantages.std() + 1e-8)
        
        # Optimize policy for K epochs
        for _ in range(self.K_epochs):
            # Evaluate old actions and values
            log_probs, state_values, dist_entropy = self.policy.evaluate(old_states, old_actions)
            
            # Find ratio (pi_theta / pi_theta_old)
            ratios = torch.exp(log_probs - old_log_probs.detach())
            
            # Finding Surrogate Loss
            surr1 = ratios * advantages
            surr2 = torch.clamp(ratios, 1 - self.eps_clip, 1 + self.eps_clip) * advantages
            
            # Final PPO loss = -min(surr1, surr2) - value loss + entropy bonus
            loss = -torch.min(surr1, surr2) + 0.5 * self.MseLoss(state_values.squeeze(), rewards) - 0.01 * dist_entropy
            loss = loss.mean()
            
            # Take gradient step
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
        
        # Copy new weights into old policy
        self.policy_old.load_state_dict(self.policy.state_dict())