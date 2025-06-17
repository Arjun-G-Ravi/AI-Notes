import gymnasium as gym

class Environment:
    def __init__(self, render_mode='human'):
        self.env = gym.make('CartPole-v1', render_mode=render_mode)
        self.done = False
        self.tot_reward = 0
        self.obs = [0. for _ in range(4)]
    
    def get_actions(self):
        return list(range(self.env.action_space.n))
    
    def is_done(self):
        return self.done
    
    def step(self, action):
        self.obs, reward, terminated, truncated, info = self.env.step(action)
        # print('hi')
        if terminated or truncated:
            self.done = True
        return self.obs, reward, terminated, truncated, info # so that it stays consistent with the gym API
    
    def get_observations(self):
        return self.obs

    def reset(self):
        obs, info = self.env.reset()
        self.done = False