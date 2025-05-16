## Reinforcement Learning 
`Reinforcement learning (RL) is a type of machine learning paradigm where an agent learns how to behave in an environment by performing actions and receiving feedback in the form of rewards or punishments.` 
- The goal of the agent is to maximize the cumulative reward over time by discovering a strategy, or policy, that maps from states of the environment to actions.
- You have an agent interacting with the environment. It makes some actions and the environment sends back the reward for that particular action and also the next state of the environment.
- In RL, we don't think in terms of 'good' actions. An action is considered 'good' if it is a part of a good policy (sequence of actions that lead to the goal state).

#### Key components:
- `Agent`: The AI or algorithm that learns and makes decisions.
- `Environment`: The world or system the agent interacts with.
- `State` (S): A snapshot of the current situation in the environment.
- `Action` (A): A choice the agent can make in a given state.
- `Reward` (R): Feedback from the environment. It can be positive (reward) or negative (penalty). This tells the agent how good or bad its last action was in that state.
- `Policy` (π): The agent's strategy or "brain." It's a mapping(function) from states to actions – what action the agent should take in a particular state. The goal of RL is to find the optimal policy.
- `Value Function` (V or Q): Predicts the expected future reward an agent can get from being in a particular state (V) or from taking a particular action in a particular state (Q). This helps the agent make long-term plans. `Q is a function that tells us the amount of reward we can expect starting from a specific state and picking a specific action whereas V tells us the amount of reward we can expect in a state.` RL agents which use these are called value-based agents.
- `Episode`: A sequence of states, actions, and rewards that ends in a terminal state (e.g., winning or losing a game, a task being completed).


## Practical Advice for Starting:
1. Start with PPO or SAC: For most continuous control problems, PPO is a great first try due to its stability and widespread use. SAC is often used when you want to push for slightly better performance and are comfortable with its complexity.
2. For Discrete Actions, use DQN variants: If your actions are discrete, start with a well-implemented DQN variant (like the one in Stable Baselines3 which includes many improvements).
3. Use Existing Libraries: Do NOT implement these from scratch unless it's for learning purposes. Use robust libraries like:
   - Stable Baselines3: Excellent for standard algorithms (PPO, SAC, TD3, DQN, A2C) with PyTorch. Well-documented and easy to use.
   - Ray RLLib: A more scalable library that supports a wider range of algorithms and distributed training.
   - TensorForce, Keras-RL, etc.: Other options exist, but Stable Baselines3 and RLLib are currently very popular and well-maintained.
4. Hyperparameter Tuning is Crucial: RL algorithms are notoriously sensitive to hyperparameters. Be prepared to experiment with learning rates, discount factors, network architectures, etc. Libraries often provide good default values, but they might not be optimal for your specific task.