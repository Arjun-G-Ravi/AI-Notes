import gymnasium as gym

class Environment:
    def __init__(self):
        self.env = gym.make('CartPole-v1')
        self.is_done = False
    
    def get_actions(self):
        return self.env.action_space # discrete class
    
    def is_done(self):
        return self.is_done
    
    def reward(self, action):
        pass
        # return reward

class Agent:
    def __init__(self):
        pass
        
        
    def step(self):
        pass



cartpoleEnv = Environment()

print(cartpoleEnv.env.action_space[0])