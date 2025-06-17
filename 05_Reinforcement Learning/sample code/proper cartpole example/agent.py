import random

class Agent:
    def __init__(self, env):
        self.env = env
        
    def select_action(self):
        return random.choice(self.env.get_actions())

    def learn(self):
        pass