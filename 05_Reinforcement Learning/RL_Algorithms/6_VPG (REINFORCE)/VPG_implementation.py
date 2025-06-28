# import random
# import torch
# import torch.nn as nn
# import numpy as np
# import gymnasium as gym


# class VPGPolicy(nn.Module):
#     def __init__(self):
#         super(VPGPolicy, self).__init__()
#         self.l1 = nn.Linear(4, 10)
#         self.relu = nn.ReLU()
#         self.l2 = nn.Linear(10, 1)
    
#     def forward(self, X):
#         return self.l2(self.relu(self.l1(X)))


# class Agent:
#     def __init__(self, env):
#         self.env = env
#         self.model = VPGPolicy()
#         self.loss_category = nn.MSELoss()
#         self.optimiser = torch.optim.AdamW(self.model.parameters(), lr=0.01)

#     def select_action(self):
#         action = int(self.model(torch.tensor(self.env.obs)) > 0.5)
#         return action

#     def learn(self, n_episodes = 100):
#         '''incomplete'''
#         for episode in range(n_episodes):
#             self.env.reset()
#             tot_reward = 0
#             while not self.env.is_done():
#                 action = self.select_action()
#                 obs, reward, _, _, _ = self.env.step(action)
#                 tot_reward += reward
            


# class Environment:
#     def __init__(self, render_mode='human'):
#         self.env = gym.make('CartPole-v1', render_mode=render_mode)
#         self.done = False
#         self.tot_reward = 0
#         self.obs = [0. for _ in range(4)]
#         self.done = False
    
#     def get_actions(self):
#         return list(range(self.env.action_space.n))

#     def step(self, action):
#         self.obs, reward, terminated, truncated, info = self.env.step(action)
#         if terminated or truncated:
#             self.done = True

#         return self.obs, reward, terminated, truncated, info # so that it stays consistent with the gym API
#     def reset(self):
#         obs, info = self.env.reset()
#         self.done = False

                