import pygame
import random
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from collections import deque
import sys
import time

# Snake Game Environment
class SnakeGame:
    def __init__(self, width=15, height=15):
        """Initialize the Snake game with a grid and Pygame display."""
        self.width = width  # Grid width
        self.height = height  # Grid height
        self.cell_size = 40  # Size of each grid cell in pixels
        pygame.init()  # Initialize Pygame
        self.screen = pygame.display.set_mode((self.width * self.cell_size, self.height * self.cell_size))  # Create display window
        self.clock = pygame.time.Clock()  # Clock for controlling frame rate
        self.reset()  # Reset game to initial state

    def reset(self):
        """Reset the game to initial state and return initial state."""
        self.snake = [(self.width // 2, self.height // 2)]  # Start snake at center
        self.direction = 0  # Initial direction: 0=up, 1=right, 2=down, 3=left
        self.food = self._place_food()  # Place food randomly
        self.score = 0  # Initialize score
        self.done = False  # Game not over
        return self.get_state()  # Return initial state

    def _place_food(self):
        """Place food at a random position not occupied by the snake."""
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if (x, y) not in self.snake:
                return (x, y)

    def get_next_direction(self, action):
        """Determine next direction based on action (0=straight, 1=left, 2=right)."""
        if action == 0:  # Continue in current direction
            return self.direction
        elif action == 1:  # Turn left
            return (self.direction - 1) % 4
        elif action == 2:  # Turn right
            return (self.direction + 1) % 4

    def step(self, action):
        """Execute one step of the game based on action and return state, reward, done."""
        if self.done:
            return self.get_state(), 0, True  # Return if game is over

        self.direction = self.get_next_direction(action)  # Update direction
        head_x, head_y = self.snake[0]  # Current head position
        if self.direction == 0:  # Move up
            new_head = (head_x, head_y - 1)
        elif self.direction == 1:  # Move right
            new_head = (head_x + 1, head_y)
        elif self.direction == 2:  # Move down
            new_head = (head_x, head_y + 1)
        elif self.direction == 3:  # Move left
            new_head = (head_x - 1, head_y)

        # Check for collision with walls or self
        if (new_head[0] < 0 or new_head[0] >= self.width or
            new_head[1] < 0 or new_head[1] >= self.height or
            new_head in self.snake):
            self.done = True
            reward = -5  # Penalty for dying
        else:
            self.snake.insert(0, new_head)  # Add new head
            if new_head == self.food:  # If food is eaten
                self.score += 1
                self.food = self._place_food()  # Place new food
                reward = 10  # Reward for eating
            else:
                self.snake.pop()  # Remove tail if no food eaten
                reward = -0.01  # Small penalty per step
        # time.sleep(0.1)
        return self.get_state(), reward, self.done

    def get_state(self):
        """Return current state as an 11-element vector."""
        head_x, head_y = self.snake[0]  # Snake head position
        food_x, food_y = self.food  # Food position
        # One-hot encoding of current direction
        dir_vec = [int(self.direction == i) for i in range(4)]
        # Check dangers for each possible action (straight, left, right)
        dangers = []
        for a in range(3):
            next_dir = self.get_next_direction(a)
            if next_dir == 0:
                nh = (head_x, head_y - 1)
            elif next_dir == 1:
                nh = (head_x + 1, head_y)
            elif next_dir == 2:
                nh = (head_x, head_y + 1)
            elif next_dir == 3:
                nh = (head_x - 1, head_y)
            # 1 if next move leads to collision, 0 otherwise
            danger = int(nh[0] < 0 or nh[0] >= self.width or
                         nh[1] < 0 or nh[1] >= self.height or
                         nh in self.snake)
            dangers.append(danger)
        # Relative food position indicators
        food_left = int(food_x < head_x)
        food_right = int(food_x > head_x)
        food_up = int(food_y < head_y)
        food_down = int(food_y > head_y)
        # Combine into state vector: [direction(4), dangers(3), food_dir(4)]
        state = dir_vec + dangers + [food_left, food_right, food_up, food_down]
        return np.array(state, dtype=np.float32)

    def render(self):
        """Render the game state to the Pygame display."""
        self.screen.fill((0, 0, 0))  # Clear screen with black background
        # Draw snake body (green)
        for x, y in self.snake[1:]:
            pygame.draw.rect(self.screen, (0, 255, 0), (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
        # Draw snake head (red)
        head_x, head_y = self.snake[0]
        pygame.draw.rect(self.screen, (255, 0, 0), (head_x * self.cell_size, head_y * self.cell_size, self.cell_size, self.cell_size))
        # Draw food (blue)
        food_x, food_y = self.food
        pygame.draw.rect(self.screen, (0, 0, 255), (food_x * self.cell_size, food_y * self.cell_size, self.cell_size, self.cell_size))
        pygame.display.update()  # Update display

# Policy Network for PPO
class PolicyNetwork(nn.Module):
    def __init__(self):
        """Initialize neural network for policy and value estimation."""
        super(PolicyNetwork, self).__init__()
        self.fc1 = nn.Linear(11, 128)  # Input: 11 state features, output: 64
        self.fc2 = nn.Linear(128, 128)  # Hidden layer
        self.fc3 = nn.Linear(128, 64)  # Hidden layer
        self.norm1 = nn.LayerNorm(128)
        self.norm2 = nn.LayerNorm(128)
        self.fc_policy = nn.Linear(64, 3)  # Output: 3 actions (straight, left, right)
        self.fc_value = nn.Linear(64, 1)  # Output: state value

    def forward(self, x):
        """Forward pass to compute action probabilities and state value."""
        # x = F.relu(self.fc1(x))  # First hidden layer with ReLU
        # x = F.relu(self.fc2(x))  # Second hidden layer with ReLU
        x = self.norm1(F.relu(self.fc1(x)))
        x = self.norm2(F.relu(self.fc2(x)))
        x = F.relu(self.fc3(x))
        
        policy = F.softmax(self.fc_policy(x), dim=-1)  # Action probabilities
        value = self.fc_value(x)  # State value
        return policy, value

# PPO Agent
class PPOAgent:
    def __init__(self):
        """Initialize PPO agent with policy network and training parameters."""
        self.policy = PolicyNetwork()  # Neural network
        self.optimizer = torch.optim.Adam(self.policy.parameters(), lr=1e-3)  # Adam optimizer
        self.gamma = 0.99  # Discount factor for rewards
        self.eps_clip = 0.2  # PPO clipping parameter
        self.memory = []  # Store experiences

    def store(self, state, action, reward, next_state, done):
        """Store an experience tuple in memory."""
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        """Select an action based on current policy."""
        state_tensor = torch.from_numpy(state).float()  # Convert state to tensor
        probs, _ = self.policy(state_tensor)  # Get action probabilities
        action = torch.multinomial(probs, 1).item()  # Sample action
        return action

    def compute_returns(self, rewards, dones):
        """Compute discounted returns for the episode."""
        returns = []
        R = 0
        for r, d in zip(reversed(rewards), reversed(dones)):
            if d:  # Reset return at episode end
                R = 0
            R = r + self.gamma * R  # Accumulate discounted reward
            returns.insert(0, R)
        return returns

    def train(self):
        """Train the policy network using PPO algorithm."""
        if not self.memory:
            return  # Skip if no experiences
        # Unpack experiences
        states, actions, rewards, next_states, dones = zip(*self.memory)
        returns = self.compute_returns(rewards, dones)  # Compute returns
        states = torch.from_numpy(np.array(states)).float()  # Convert to tensor
        actions = torch.tensor(actions)
        returns = torch.tensor(returns).float()

        # Compute old policy log probabilities and advantages
        probs, values = self.policy(states)
        dist = torch.distributions.Categorical(probs)
        log_probs = dist.log_prob(actions)
        advantages = (returns - values.squeeze()).detach()  # Detach to avoid graph reuse

        # Perform PPO updates
        for _ in range(3):  # Number of PPO epochs
            probs, values = self.policy(states)  # Recompute with current policy
            dist = torch.distributions.Categorical(probs)
            new_log_probs = dist.log_prob(actions)
            ratio = torch.exp(new_log_probs - log_probs.detach())  # Policy ratio
            surr1 = ratio * advantages  # Surrogate objective 1
            surr2 = torch.clamp(ratio, 1 - self.eps_clip, 1 + self.eps_clip) * advantages  # Clipped objective
            policy_loss = -torch.min(surr1, surr2).mean()  # PPO policy loss
            value_loss = F.mse_loss(values.squeeze(), returns)  # Value function loss
            loss = policy_loss + 0.5 * value_loss  # Combined loss

            self.optimizer.zero_grad()  # Clear gradients
            loss.backward()  # Compute gradients
            self.optimizer.step()  # Update weights

        self.memory.clear()  # Clear memory after training

# Main Loop
FPS = 3000  # Frames per second for rendering
if __name__ == "__main__":
    """Run the training loop for the Snake game with PPO."""
    env = SnakeGame()  # Initialize game environment
    agent = PPOAgent()  # Initialize PPO agent
    episodes = 1000  # Number of training episodes
    max_snake_steps = 0
    total_rewards = deque(maxlen=20)  # Track last 100 episode rewards
    top_score = 0
    for episode in range(episodes):
        if episode % 20 == 0:
            max_snake_steps += 5
            print('Max steps updated to', max_snake_steps)
        snake_steps = 0
        state = env.reset()  # Reset environment
        done = False
        episode_reward = 0
        while not done:
            snake_steps += 1
            action = agent.act(state)  # Select action
            next_state, reward, done = env.step(action)  # Execute action
            agent.store(state, action, reward, next_state, done)  # Store experience
            state = next_state  # Update state
            episode_reward += reward
            episode_reward = round(episode_reward, 3)
            # env.render()  # Render game
            for event in pygame.event.get():  # Handle Pygame events
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if snake_steps >= max_snake_steps:
                done = True
            env.clock.tick(FPS)  # Control frame rate
        agent.train()  # Train policy
        total_rewards.append(episode_reward)  # Track reward
        avg_reward = np.mean(total_rewards)  # Compute average reward
        top_score = max(top_score, env.score)
        print(f"Episode {episode + 1}, Reward: {episode_reward}, Avg Reward: {avg_reward:.2f}, Score: {env.score}, Top score:{top_score}")
        # if avg_reward > 50:  # Stop if average reward exceeds threshold
        #     print("Training completed!")
        #     break