# Value Iteration Technique
Value Iteration is a dynamic programming algorithm used to compute the optimal policy and value function for Markov Decision Processes (MDPs). It iteratively updates the value function until it converges to the optimal value function. The key idea is to use the Bellman equation to update the value of each state based on the expected rewards from taking actions in that state and transitioning to subsequent states.

For each state, we look into the possible actions, compute the expected value of each action (considering the rewards and the values of the next states), and update the value of the current state to be the maximum expected value across all actions. This is a recursive process that continues until the value function stabilizes (i.e., the changes in values are below a certain threshold).

- The disadvantage of Value Iteration is that it can be computationally expensive for large state spaces, as it requires iterating over all states and actions repeatedly. However, it guarantees convergence to the optimal value function under certain conditions.
- Another disadvantage is that it requires a complete model of the environment, including transition probabilities and rewards, which may not be available in real-world scenarios.
- Also, it is not suitable for environments with continuous state or action spaces, as it relies on discrete states and actions.
- Most of the times, many of the states will not be reachable, and hence, the algorithm will waste time updating the values of those unreachable states.