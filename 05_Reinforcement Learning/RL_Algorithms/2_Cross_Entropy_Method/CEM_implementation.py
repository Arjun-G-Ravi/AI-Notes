'''
Here I've implemented a trick which will remove last 'n' actions when training.
This leads to the model getting better training data to be trained on, and essentially training.
Note that this is not consistent

'''


import torch
import gymnasium as gym

class Agent:
    def __init__(self, env):
        self.env = env
        self.distribution_mean_w1 = 0.
        self.distribution_mean_w2 = 0.
        self.distribution_mean_w3 = 0.
        self.distribution_mean_w4 = 0.
        self.distribution_mean_b = 0.

        self.distribution_std_w1 = 1.
        self.distribution_std_w2 = 1.
        self.distribution_std_w3 = 1.
        self.distribution_std_w4 = 1.
        self.distribution_std_b = 1.
        self.W = None
        self.b = None

    def predict(self, obs):
        obs = torch.tensor(obs)
        W_1 = torch.normal(mean=self.distribution_mean_w1, std=self.distribution_std_w1, size=(1,))
        W_2 = torch.normal(mean=self.distribution_mean_w2, std=self.distribution_std_w2, size=(1,))
        W_3 = torch.normal(mean=self.distribution_mean_w3, std=self.distribution_std_w3, size=(1,))
        W_4 = torch.normal(mean=self.distribution_mean_w4, std=self.distribution_std_w4, size=(1,))

        self.W = torch.tensor([W_1, W_2, W_3, W_4])
        self.b = torch.normal(mean=self.distribution_mean_b, std=self.distribution_std_b, size=(1,))
        return int(torch.sigmoid(self.W@obs + self.b) > 0.5)

    def learn(self, num_epochs = 10, bs = 100):
        for epoch in range(num_epochs):
            W_history = []
            b_history = []
            done = False
            while not done:
                obs = self.env.obs
                action = self.predict(obs)
                self.env.step(action)
                done = self.env.done

                if not done:
                    # technically this would contain all "1" rewarded actions
                    W_history.append(self.W)
                    b_history.append(self.b)
                    assert self.W != None
                    assert self.b != None
            print(self.env.tot_reward)
            W_history = W_history[:10] # the trick mentioned above
            b_history = b_history[:10]
            if not W_history: return
            W_history = torch.stack(W_history)
            b_history = torch.stack(b_history)
            # episode is over
            self.update_distribution(W_history, b_history)
            self.env.reset()

    def update_distribution(self, W_history, b_history):
        self.distribution_mean_w1 = W_history[:, 0].mean()
        self.distribution_mean_w2 = W_history[:, 1].mean()
        self.distribution_mean_w3 = W_history[:, 2].mean()
        self.distribution_mean_w4 = W_history[:, 3].mean()
        self.distribution_mean_b = b_history.mean()

        self.distribution_std_w1 = W_history[:, 0].std()
        self.distribution_std_w2 = W_history[:, 1].std()
        self.distribution_std_w3 = W_history[:, 2].std()
        self.distribution_std_w4 = W_history[:, 3].std()
        self.distribution_std_b = b_history.std()

    

            
        
            
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


if __name__ == '__main__':
    env = Environment('')
    agent = Agent(env)
    env.reset()

    # training
    agent.learn(num_epochs=1000)

    # inference
    ct = 0
    while ct < 10:
        obs = env.obs
        act = agent.predict(obs)
        env.step(act)
        if env.done:
            print(env.tot_reward)
            env.reset()
            ct += 1
