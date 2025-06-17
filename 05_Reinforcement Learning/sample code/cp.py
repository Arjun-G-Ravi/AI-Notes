# Random cartpole

import gymnasium as gym

if __name__ == "__main__":
    # For gymnasium or latest gym, use render_mode="human"
    env = gym.make("CartPole-v1", render_mode="human")

    total_reward = 0.0
    total_steps = 0
    obs, info = env.reset()
    
    for i in range(10):
        while True:
            env.render()  # Show the environment
            action = env.action_space.sample()
            obs, reward, terminated, truncated, info = env.step(action)
            total_reward += reward
            total_steps += 1
            if terminated or truncated:
                break
        print('Reward:', total_reward)
        env.reset()
        total_reward = 0