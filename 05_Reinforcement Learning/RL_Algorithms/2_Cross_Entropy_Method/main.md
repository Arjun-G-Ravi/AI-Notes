# Cross Entropy Method (CEM)

CEM is a model-free reinforcement learning algorithm that optimizes policies by sampling from a distribution and updating the parameters based on the best-performing samples. It is particularly useful for high-dimensional action spaces and can be applied to both discrete and continuous action spaces.

Just like Hill Climbing, CEM is not a traditional RL algorithm but can be used to optimize policies in RL. It is a black-box optimization method that does not require knowledge of the environment's dynamics.

I've used CEM in two different ways:
1. Action Space Optimization: CEM can be used to optimize the parameters of a policy directly by sampling actions from a distribution and updating the distribution based on the performance of the sampled actions.
2. Policy Optimization: CEM can be used to optimize the parameters of a policy by sampling trajectories from the environment and updating the policy based on the performance of the sampled trajectories. So, it would be like action = sign(W *obs + b) where W and b are the parameters of the policy. We can sample distributions for W and b, and update them based on the performance of the sampled actions.