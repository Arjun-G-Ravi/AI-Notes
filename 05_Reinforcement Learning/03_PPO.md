# Proximal Policy Approximation(PPO)

PPO is one of the most popular and widely used reinforcement learning algorithms today, known for its good balance of performance, implementation simplicity, and stability. It was introduced by John Schulman and team at OpenAI in 2017 as an improvement upon Trust Region Policy Optimization (TRPO).

# What is PPO?
- Type: PPO is an on-policy, actor-critic reinforcement learning algorithm.
- Goal: To train a policy network (the "actor") that maps states to actions, and often a value network (the "critic") that estimates the value of states, with the aim of maximizing the expected cumulative reward.
- Core Idea: To perform policy updates iteratively, similar to standard policy gradient methods, but with a mechanism that constrains the updates to be relatively small. This prevents the policy from changing too drastically in a single step, which can lead to catastrophic performance drops (a common issue in policy gradient methods).

# Why PPO?
- Vanilla Policy Gradient (VPG) / REINFORCE have a big issue to choosing the correct learning rate.
- Trust Region Policy Optimization (TRPO) solves this issue but is computationally expensive and complex to implement.
- PPO aims to achieve a similar effect as TRPO – constrained updates for stability – but with a simpler, first-order optimization approach. It does this primarily through a clipped surrogate objective function.

