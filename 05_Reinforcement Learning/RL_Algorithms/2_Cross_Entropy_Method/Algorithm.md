# Algorithm of Cross Entropy Method (CEM)

1. Initialize a random policy - which will be a distribution over actions. Such a distribution can be done using a Gaussian distribution with mean and standard deviation.
2. Sample a set of actions from the policy distribution.
3. Evaluate the sampled actions by running them in the environment and calculating the rewards.
4. Select the top-performing actions(Elite actions) based on the rewards.
5. Update the policy distribution parameters (mean and standard deviation) based on the elite actions. This can be done using maximum likelihood estimation or other optimization techniques.
6. Repeat steps 2-5 until convergence or a stopping criterion is met.