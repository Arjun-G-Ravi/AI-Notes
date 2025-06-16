# Classification of RL Algorithms
![alt text](image-6.png)

In the highest level, we can classify RL algorithms into two main categories: Model-based and Model-free.
## Model-based RL
Model-based RL algorithms build a model of the environment and use it to make decisions. They can plan ahead by simulating future states and actions, which allows them to make more informed decisions. A model is nothing but a function that predicts state transitions and rewards. They are generally more sample efficient because they can learn from fewer interactions with the environment, but are harder to develop and require more computational resources.

## Model-free RL
Model-free RL algorithms do not build a model of the environment. Instead, they learn directly from the interactions with the environment. They can be further classified into three main categories: Value-based, Policy-based and Actor-Critic methods.

### Value-based RL
- They try to approximate the optimal action-value function (Q-value) or state-value function (V-value).
- The agent then selects actions based on these values. The most common value-based RL algorithm is Q-learning, which learns the Q-value function.
- Examples: Q-learning, Deep Q-Networks (DQN), SARSA.

### Policy-based RL
- Directly learn the policy (the mapping from states to actions) without using a value function.
- They optimize the policy(generally neural networks) by maximizing the expected cumulative reward. This is often done using gradient ascent methods, where the policy is updated in the direction of the gradient of the expected reward with respect to the policy parameters.
- These algorithms can handle high-dimensional action spaces and are often used in continuous action environments. 
- Examples: REINFORCE, Policy Gradient 

### Actor-Critic Methods
- Combine both policy-based and value-based approaches.
- Use two models: an actor (learns the policy) and a critic (learns the value function).
- Example: A2C, DDPG, PPO.

# On-policy vs Off-policy
**On-Policy RL**
- In on-policy methods, the agent learns about the policy it is currently following.
- The actions used to update the agent are those actually taken by the current policy.
- The same policy is used for both exploring the environment and for learning.
- **Example algorithms:** SARSA, A2C (Advantage Actor-Critic)
- **Key point:** Learning is based on the behavior of the current policy.

**Off-Policy RL**
- In off-policy methods, the agent learns about a different policy than the one used to generate the data.
- The agent can learn from experiences gathered by any policy (including old policies or even random behavior).
- This allows using past data or data collected by another agent.
- **Example algorithms:** Q-learning, DDPG
- **Key point:** Learning is based on the target policy, but experience can come from other (behavior) policies.