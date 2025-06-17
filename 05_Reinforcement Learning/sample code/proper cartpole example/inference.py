from agent import Agent
from environment import Environment

cartPoleEnv = Environment()
randomAgent = Agent(cartPoleEnv)
for _ in range(10):

    tot_reward = 0
    cartPoleEnv.reset()
    while not cartPoleEnv.is_done():
        action = randomAgent.select_action()
        obs, reward, _, _, _ = cartPoleEnv.step(action)
        tot_reward += reward
        # print(cartPoleEnv.get_observations())
    print(tot_reward)