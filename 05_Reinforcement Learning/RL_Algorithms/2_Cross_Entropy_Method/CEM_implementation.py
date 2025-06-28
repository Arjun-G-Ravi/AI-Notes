import random
import torch
import torch.nn as nn
import gymnasium as gym

class Agent:
    def __init__(self, env):
        self.env = env
        self.distribution_mean = 0.
        self.distribution_std = 1.

    def select_action(self):
        return torch.normal(mean=self.distribution_mean, std=self.distribution_std, size=(1,))

    
    def predict(self, obs):
        # use the current model and sample an action
        action = int(self.select_action() > 0)
        return action

    def learn(self, n_episodes = 100):
        # add this
        ...

            
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