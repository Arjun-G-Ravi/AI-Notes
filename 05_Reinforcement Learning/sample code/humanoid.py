from stable_baselines3 import PPO
import gymnasium as gym
env_name = "Humanoid-v5"

env = gym.make(env_name, render_mode="rgb_array")
model = PPO('MlpPolicy', env, device='cpu', verbose=1)

def run_eval_env(model, num_runs=1, env_name=env_name):
    eval_env = gym.make(env_name, render_mode="human")
    episode_rew = 0
    state, info = eval_env.reset()
    curr_run = 0
    while curr_run < num_runs:
        action, _states = model.predict(state, deterministic=True)
        state, reward, done, truncated, info = eval_env.step(action)
        episode_rew += reward
        eval_env.render()

        if truncated or done:
            print('Reward:', episode_rew)
            episode_rew = 0
            state, info = eval_env.reset()
            curr_run += 1

    eval_env.close()

model.learn(total_timesteps=1000, progress_bar=True)
run_eval_env(model, num_runs=3)