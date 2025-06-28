# Q-Learning
Q-learning is a model-free reinforcement learning algorithm used to learn the value of an action in a particular state. It is an optimisation over the value iteration technique, allowing an agent to learn how to act optimally in an environment without needing a model of that environment. Also, it computes the Q-value of a (state, action) pair, only when the agent takes that action in that state, rather than updating the value of all states and actions as in value iteration. This makes it more efficient in many scenarios, especially when the state space is large or continuous.

### Q-Table
A Q-table is a table where each row represents a state and each column represents an action. The values in the table represent the expected utility (Q-value) of taking a particular action in a particular state. The Q-value is updated based on the reward received after taking an action and the maximum expected future rewards from the next state (found out using Bellman's Equation). The Q-table is used to derive the optimal policy by selecting the action with the highest Q-value for each state.

### How update happens in Q-table
- One way to update the Q-table is to rewrite the Q-value of the (state, action) pair using the Bellman equation: `Q(s, a) = r + γ * Q(s', a')`
- The problem with this approach is that it can lead to oscillations and instability in the Q-values, especially in environments with high variability in rewards or transitions.

- To address this, a more stable update rule is used:
  `Q(s, a) = Q(s, a) + α * [(r + γ * Q(s', a')) - Q(s, a)]`
which is equivalent to:`Q(s, a) = [1 - α] * Q(s, a) + α * [r + γ * Q(s', a')]`
where, 
- `Q(s', a')` is the maximum Q-value for the next state `s'` over all possible actions `a'`.

- This update rule is based on the idea of `temporal difference` learning, where the Q-value is updated incrementally based on the difference between the current Q-value and the expected future rewards. The learning rate `α` controls how much the new information overrides the old information, and `γ` is the discount factor that determines the importance of future rewards.