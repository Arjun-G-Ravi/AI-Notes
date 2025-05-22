import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.vec_env import DummyVecEnv

ENV_ID = 'LunarLander-v3'
TRAIN_TIMESTEPS = 1000
EVAL_EPISODES = 5

print(f"Training PPO on {ENV_ID} for {TRAIN_TIMESTEPS} timesteps...")

train_env = make_vec_env(ENV_ID, n_envs=1, seed=0, vec_env_cls=DummyVecEnv)

model = PPO("MlpPolicy", train_env, verbose=1, device='cpu')

model.learn(total_timesteps=TRAIN_TIMESTEPS)

print("Training finished.")

print(f"\nEvaluating trained agent for {EVAL_EPISODES} episodes...")

eval_env = gym.make(ENV_ID, render_mode='human')

obs, info = eval_env.reset()

episode_count = 0
while episode_count < EVAL_EPISODES:
    action, _states = model.predict(obs, deterministic=True)

    obs, reward, done, truncated, info = eval_env.step(action)

    eval_env.render()

    if done or truncated:
        print(f"Episode {episode_count + 1} finished.")
        obs, info = eval_env.reset()
        episode_count += 1

eval_env.close()
print("Evaluation finished.")