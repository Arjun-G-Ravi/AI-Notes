import gymnasium as gym

class Environment:
    def __init__(self):
        self.env = gym.make('CartPole-v1', render_mode='human')
        self.is_done = False
        self.tot_reward = 0
        self.obs
    
    def get_actions(self):
        return self.env.action_space # discrete class
    
    def is_done(self):
        return self.is_done
    
    def action(self, action):
        '''Takes action and returns reward'''
        obs, reward, terminated, truncated, info = self.env.step(action)
        if terminated or truncated:
            self.is_done = True
        self.obs = obs
        return reward

class Agent:
    def __init__(self, env):
        self.env = env
        
    def step(self):
        pass



cartpoleEnv = Environment()
RandomAgent = Agent(cartpoleEnv)
print(cartpoleEnv.env.action_space[0])