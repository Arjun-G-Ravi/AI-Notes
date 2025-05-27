## Reinforcement Learning 
`Reinforcement learning (RL) is a type of machine learning paradigm where an agent learns how to behave in an environment by performing actions and receiving feedback in the form of rewards or punishments.` 
- The goal of the agent is to maximize the cumulative reward over time by discovering a strategy, or policy, that maps from states of the environment to actions.
- You have an agent interacting with the environment. It makes some actions and the environment sends back the reward for that particular action and also the next state of the environment.
- In RL, we don't think in terms of 'good' actions. An action is considered 'good' if it is a part of a good policy (sequence of actions that lead to the goal state).

#### Key components:
- `Agent`: The AI or algorithm that learns and makes decisions.
- `Environment`: The world or system the agent interacts with.
- `State` (S): A snapshot of the current situation in the environment. It is a function of the history of the environment and the agent's actions. 
- `Action` (A): A choice the agent can make in a given state.
- `Reward` (R): Feedback from the environment. This tells the agent how good or bad its last action was in that state.
- `Policy` (π): The agent's strategy or "brain." It's a function from states to actions – what action the agent should take in a particular state. The goal of RL is to find the optimal policy. It can be deterministic (always the same action for a state) or stochastic (probabilistic action selection, ie, gives the probability for taking each action, given a state).
- `Value Function` (V or Q): Predicts the expected future reward an agent can get from being in a particular state (V) or from taking a particular action in a particular state (Q). This helps the agent make long-term plans. `Q is a function that tells us the amount of reward we can expect starting from a specific state and picking a specific action(and then follow a policy) whereas V tells us the amount of reward we can expect in a state(and then follow a policy).` RL agents which use these are called value-based agents.
- `Episode`: A sequence of states, actions, and rewards that ends in a terminal state .