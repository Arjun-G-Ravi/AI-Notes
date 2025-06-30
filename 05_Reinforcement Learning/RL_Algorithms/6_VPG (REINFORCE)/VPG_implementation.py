import torch
import torch.nn as nn
import torch.optim as optim
from torch.distributions import Categorical
import gym

# Hyperparameters
learning_rate = 1e-3
gamma = 0.98
n_rollouts = 10

class Policy(nn.Module):
    def __init__(self):
        super(Policy, self).__init__()
        self.data = []  # Stores (reward, action_prob) tuples for each step

        # Simple feedforward neural network
        self.fc1 = nn.Linear(4, 128)  # Input: state (4 dims), Hidden: 128 units
        self.fc2 = nn.Linear(128, 2)  # Output: action probabilities (2 actions)
        self.optimizer = optim.Adam(self.parameters(), lr=learning_rate)

    def forward(self, x):
        x = torch.relu(self.fc1(x))  # Hidden layer with ReLU activation
        x = torch.softmax(self.fc2(x), dim=0)  # Output layer with softmax for probabilities
        return x

    def put_data(self, item):
        self.data.append(item)  # Store (reward, action_prob) for training

    def train_net(self):
        R = 0  # Initialize return
        self.optimizer.zero_grad()
        # Iterate over collected data in reverse (for reward-to-go calculation)
        for r, prob in self.data[::-1]:
            R = r + gamma * R  # Discounted return
            loss = -torch.log(prob) * R  # Policy gradient loss
            loss.backward()
        self.optimizer.step()  # Update policy network
        self.data = []  # Clear data after training

def main():
    env = gym.make('CartPole-v1')
    pi = Policy()
    score = 0.0
    print_interval = 50

    for n_epi in range(1000):  # Run for many episodes
        s, _ = env.reset()  # Reset environment, get initial state
        done = False

        while not done:
            for t in range(n_rollouts):  # Collect rollouts
                prob = pi(torch.from_numpy(s).float())  # Get action probabilities from policy
                m = Categorical(prob)  # Create categorical distribution
                a = m.sample()  # Sample action
                s_prime, r, done, truncated, info = env.step(a.item())  # Take action in env
                pi.put_data((r, prob[a]))  # Store reward and action probability
                s = s_prime  # Move to next state
                score += r  # Accumulate score

                if done:
                    break  # End episode if done
            
            pi.train_net()  # Train policy after collecting rollouts

        if n_epi % print_interval == 0 and n_epi != 0:
            print(f"# of episode: {n_epi}, avg score: {score/print_interval:.1f}")
            score = 0.0  # Reset score for next interval

    env.close()

if __name__ == '__main__':
    main()