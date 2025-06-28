# doesnt work
import torch
import torch.nn as nn
from torch.distributions.categorical import Categorical
from torch.optim import Adam
import numpy as np
import gymnasium as gym
from gymnasium.spaces import Discrete, Box

def mlp(sizes, activation=nn.Tanh, output_activation=nn.Identity):
    # Build a feedforward neural network.
    layers = []
    for j in range(len(sizes)-1):
        act = activation if j < len(sizes)-2 else output_activation
        layers += [nn.Linear(sizes[j], sizes[j+1]), act()]
    return nn.Sequential(*layers)

def train(env_name='CartPole-v1', hidden_sizes=[32], lr=1e-2, 
          epochs=50, batch_size=5000, render=False, render_mode = ''):

    # make environment, check spaces, get obs / act dims
    env = gym.make(env_name, render_mode = render_mode)
    assert isinstance(env.observation_space, Box), \
        "This example only works for envs with continuous state spaces."
    assert isinstance(env.action_space, Discrete), \
        "This example only works for envs with discrete action spaces."

    obs_dim = env.observation_space.shape[0]
    n_acts = env.action_space.n

    print(f"Observation space: {env.observation_space}")
    print(f"Action space: {env.action_space}")

    # make core of policy network
    logits_net = mlp(sizes=[obs_dim]+hidden_sizes+[n_acts])

    # make function to compute action distribution
    def get_policy(obs):
        logits = logits_net(obs)
        return Categorical(logits=logits)

    # make action selection function (outputs int actions, sampled from policy)
    def get_action(obs):
        # Ensure obs is properly processed as a tensor
        obs_tensor = torch.as_tensor(obs, dtype=torch.float32)
        # Handle shape issues
        if len(obs_tensor.shape) == 1:
            # Add batch dimension if needed
            obs_tensor = obs_tensor.unsqueeze(0)
        return get_policy(obs_tensor).sample().item()

    # make loss function whose gradient, for the right data, is policy gradient
    def compute_loss(obs, act, weights):
        logp = get_policy(obs).log_prob(act)
        return -(logp * weights).mean()

    # make optimizer
    optimizer = Adam(logits_net.parameters(), lr=lr)

    # for training policy
    def train_one_epoch():
        # make some empty lists for logging.
        batch_obs = []          # for observations
        batch_acts = []         # for actions
        batch_weights = []      # for R(tau) weighting in policy gradient
        batch_rets = []         # for measuring episode returns
        batch_lens = []         # for measuring episode lengths

        # reset episode-specific variables
        obs, _ = env.reset()    # first obs comes from starting distribution
        done = False            # signal from environment that episode is over
        ep_rews = []            # list for rewards accrued throughout ep

        # render first episode of each epoch
        finished_rendering_this_epoch = False

        # collect experience by acting in the environment with current policy
        while True:

            # rendering
            if (not finished_rendering_this_epoch) and render:
                env.render()

            # save obs (ensure it's a NumPy array)
            batch_obs.append(np.array(obs, dtype=np.float32))

            # act in the environment
            act = get_action(obs)
            obs, rew, terminated, truncated, _ = env.step(act)
            done = terminated or truncated

            # save action, reward
            batch_acts.append(act)
            ep_rews.append(rew)

            if done:
                # if episode is over, record info about episode
                ep_ret, ep_len = sum(ep_rews), len(ep_rews)
                batch_rets.append(ep_ret)
                batch_lens.append(ep_len)

                # the weight for each logprob(a|s) is R(tau)
                batch_weights += [ep_ret] * ep_len

                # reset episode-specific variables
                obs, _ = env.reset()
                done, ep_rews = False, []

                # won't render again this epoch
                finished_rendering_this_epoch = True

                # end experience loop if we have enough of it
                if len(batch_obs) > batch_size:
                    break

        # Convert batch data to tensors for processing
        obs_tensor = torch.as_tensor(np.array(batch_obs), dtype=torch.float32)
        act_tensor = torch.as_tensor(np.array(batch_acts), dtype=torch.int32)
        weights_tensor = torch.as_tensor(np.array(batch_weights), dtype=torch.float32)
        
        # take a single policy gradient update step
        optimizer.zero_grad()
        batch_loss = compute_loss(obs=obs_tensor,
                                  act=act_tensor,
                                  weights=weights_tensor)
        batch_loss.backward()
        optimizer.step()
        return batch_loss, batch_rets, batch_lens

    # training loop
    for i in range(epochs):
        batch_loss, batch_rets, batch_lens = train_one_epoch()
        print('epoch: %3d \t loss: %.3f \t return: %.3f \t ep_len: %.3f'%
                (i, batch_loss, np.mean(batch_rets), np.mean(batch_lens)))

# Simplified main function without command-line arguments
if __name__ == '__main__':
    print('\nUsing simplest formulation of policy gradient.\n')
    # Set your parameters here
    env_name = 'CartPole-v1'
    render = 'human'
    learning_rate = 1e-2
    
    # Call the training function with the specified parameters
    train(env_name=env_name, render=render, lr=learning_rate, render_mode='human')