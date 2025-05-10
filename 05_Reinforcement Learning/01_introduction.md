## Reinforcement Learning - a high level overview
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
- `Value Function` (V or Q): Predicts the expected future reward an agent can get from being in a particular state (V) or from taking a particular action in a particular state (Q). This helps the agent make long-term plans.
- `Episode`: A sequence of states, actions, and rewards that ends in a terminal state (e.g., winning or losing a game, a task being completed).


# Practical Advice for Starting:
1. Start with PPO or SAC: For most continuous control problems, PPO is a great first try due to its stability and widespread use. SAC is often used when you want to push for slightly better performance and are comfortable with its complexity.
2. For Discrete Actions, use DQN variants: If your actions are discrete, start with a well-implemented DQN variant (like the one in Stable Baselines3 which includes many improvements).
3. Use Existing Libraries: Do NOT implement these from scratch unless it's for learning purposes. Use robust libraries like:
   - Stable Baselines3: Excellent for standard algorithms (PPO, SAC, TD3, DQN, A2C) with PyTorch. Well-documented and easy to use.
   - Ray RLLib: A more scalable library that supports a wider range of algorithms and distributed training.
   - TensorForce, Keras-RL, etc.: Other options exist, but Stable Baselines3 and RLLib are currently very popular and well-maintained.
4. Hyperparameter Tuning is Crucial: RL algorithms are notoriously sensitive to hyperparameters. Be prepared to experiment with learning rates, discount factors, network architectures, etc. Libraries often provide good default values, but they might not be optimal for your specific task.

# Best RL Algorithm
1. PPO (Proximal Policy Optimization):
    - What it is: A policy gradient algorithm that updates the policy in small, stable steps.
    - Why it's important: Known for its balance of performance, stability, and relative ease of implementation/tuning. It's often the default choice for many tasks.
    - Best for: General-purpose use, works well for both continuous and discrete action spaces.
2. SAC (Soft Actor-Critic):
    - What it is: An off-policy actor-critic algorithm that incorporates entropy maximization into its objective.
    - Why it's important: Currently one of the state-of-the-art algorithms, particularly for continuous control, known for high performance and good sample efficiency.
    - Best for: Continuous control tasks where achieving peak performance and robust exploration are key.
3. TD3 (Twin Delayed Deep Deterministic Policy Gradient):
    - What it is: An off-policy actor-critic algorithm that improves upon DDPG by using twin critics and delayed policy updates.
    - Why it's important: A strong alternative to SAC for continuous control, specifically designed to combat issues like Q-value overestimation, leading to more stable training than its predecessor.
    - Best for: Continuous control tasks, especially if stability is a concern.
4. DQN (and its variants):
    - What it is: A value-based algorithm that uses a deep neural network to approximate the Q-function. Variants like Double DQN, Dueling DQN, and Prioritized Experience Replay add significant improvements.
    - Why it's important: The foundational deep RL algorithm for discrete action spaces. Its modern variants are state-of-the-art for problems like playing Atari games.
    - Best for: Environments with discrete action spaces.
5. Model-Based RL (e.g., MBPO - Model-Based Policy Optimization):
    - What it is: A class of algorithms that learn a model of the environment's dynamics and use this model to plan or generate synthetic data for training.
    - Why it's important: Can be significantly more sample-efficient than model-free methods, requiring less interaction with the real environment.
    - Best for: Scenarios where interacting with the environment is expensive or slow (e.g., real-world robotics).