These include RL algorithms that I am learning and/or implementing. The list is not exhaustive and will be updated as I learn more algorithms.

Current plan

1. Hill climbing
2. CEM
3. Value Iteration
4. Q-learning
5. REINFORCE
6. Vanilla Policy Gradient
7. TRPO
8. PPO
9. DDPG
10. SAC

# Basic Algorithm


```python
import random
import torch
import torch.nn as nn
import numpy as np
import gymnasium as gym

class Agent:
    def __init__(self, env):
        self.env = env

    def select_action(self):
        action = int(self.model(torch.tensor(self.env.obs)) > 0.5)
        return action
    
    def predict(self, obs):
        # use the current model and sample an action
        action = random.choice([0, 1])
        return action

    def learn(self, n_episodes = 100):
        '''update the Agent to learn'''

            
class Environment:
    def __init__(self, render_mode='human'):
        self.env = gym.make('CartPole-v1', render_mode=render_mode)
        self.tot_reward = 0
        self.obs = [0. for _ in range(4)]
        self.done = False
    
    def get_actions(self):
        return list(range(self.env.action_space.n))

    def step(self, action):
        self.obs, reward, terminated, truncated, info = self.env.step(action)
        self.tot_reward += 1
        if terminated or truncated:
            self.done = True
        
        # so that it stays consistent with the gym API
        return self.obs, reward, terminated, truncated, info

    def reset(self):
        obs, info = self.env.reset()
        self.done = False
        self.tot_reward = 0


# inference
if __name__ == '__main__':
    env = Environment()
    agent = Agent(env)
    env.reset()

    ct = 0
    while ct < 10:
        obs = env.obs
        act = agent.predict(obs)
        env.step(act)
        if env.done:
            print(env.tot_reward)
            env.reset()
            ct += 1
```