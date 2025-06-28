# Algorithm of Value Iteration Technique
1. Initialize the value function for all states to zero or a small random value.
2. For each state, compute the expected value of each action based on the current value function:
   - For each action, calculate the expected reward and the value of the next state.
   - Update the value of the current state to be the maximum expected value across all actions.
3. Repeat step 2 until the value function converges (i.e., the changes in values are below a certain threshold).
