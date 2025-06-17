import random
import torch
import torch.nn as nn
import numpy as np


class RLModel(nn.Module):
    def __init__(self):
        super(RLModel, self).__init__()
        self.l1 = nn.Linear(4, 10)
        self.relu = nn.ReLU()
        self.l2 = nn.Linear(10, 1)
    
    def forward(self, X):
        return self.l2(self.relu(self.l1(X)))

class Agent:
    def __init__(self, env):
        self.env = env
        self.model = RLModel()
        self.loss_category = nn.MSELoss()
        self.optimiser = torch.optim.AdamW(self.model.parameters(), lr=0.01)


    def select_action(self):
        action = int(self.model(torch.tensor(self.env.obs)) > 0.5)
        # print(action)
        return action

        # return random.choice(self.env.get_actions())

    def learn(self, n_episodes = 100):
        for episode in range(n_episodes):
            self.env.reset()
            tot_reward = 0
            while not self.env.is_done():
                action = self.select_action()
                obs, reward, _, _, _ = self.env.step(action)
                tot_reward += reward
            
            # the run is finished



        