# Q-learning algorithm

1. Initialize the Q-table with zeros or small random values for all state-action pairs.(in practice, it is often initialized with defaultdicts)
2. Select an action based on the q-learning(generally there is randomness involved, like epsilon-greedy policy).
3. Take the action and observe the reward and the next state.
4. Update the Q-value for the current state-action pair using the Q-learning update rule:
   `Q(s, a) = Q(s, a) + α * [(r + γ * max(Q(s', a')) - Q(s, a)]`
5. Repeat steps 2-4 until the Q-values converge or a stopping criterion is met.