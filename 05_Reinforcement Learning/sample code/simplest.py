import random

class Environment:
    def __init__(self):
        self.steps_left = 10

    def get_observations(self):
        return [1,2,3]
    
    def get_actions(self):
        return [0, 1]
    
    def action(self):
        return random.choice(self.get_actions())

    def reward(self, action):
        return random.randint(-10, 10)

    def is_done(self):
        return self.steps_left == 0
    
class Agent:
    def __init__(self):
        self.tot_reward = 0

    def step(self):
        obs = env.get_observations()
        action = env.action()
        reward = env.reward(action)
        self.tot_reward += reward
        env.steps_left -= 1
        print(reward)
  

if __name__ == "__main__":
    env = Environment()
    agent = Agent()

    while not env.is_done():
        agent.step()


