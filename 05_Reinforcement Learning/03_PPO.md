# Proximal Policy Approximation(PPO)

PPO is one of the most popular and widely used reinforcement learning algorithms today, known for its good balance of performance, implementation simplicity, and stability. It was introduced by John Schulman and team at OpenAI in 2017 as an improvement upon Trust Region Policy Optimization (TRPO).

# What is PPO?
- Type: PPO is an on-policy, actor-critic reinforcement learning algorithm.
- Goal: To train a policy network (the "actor") that maps states to actions, and often a value network (the "critic") that estimates the value of states, with the aim of maximizing the expected cumulative reward.
- Core Idea: To perform policy updates iteratively, similar to standard policy gradient methods, but with a mechanism that constrains the updates to be relatively small. This prevents the policy from changing too drastically in a single step, which can lead to catastrophic performance drops (a common issue in policy gradient methods).

# Why PPO?
- Vanilla Policy Gradient (VPG) / REINFORCE have a big issue to choosing the correct learning rate. (It is just like Gradient Descent)
- Trust Region Policy Optimization (TRPO) solves this issue but is computationally expensive and complex to implement.
- PPO aims to achieve a similar effect as TRPO – constrained updates for stability – but with a simpler, first-order optimization approach. It does this primarily through a clipped surrogate objective function.

# The Core Mechanism: Clipped Surrogate Objective

PPO uses a soft constraint (a penalty or modification of the objective function) to discourage large policy changes. 
![alt text](image-1.png)

![alt text](image-2.png)


5. Key Components & Concepts
Actor-Critic Architecture: PPO typically uses two neural networks (or a single network with two heads):
Actor (
π
θ
π 
θ
​
 
): Takes state 
s
s
 as input and outputs probabilities over actions (discrete action space) or parameters of a distribution (e.g., mean and standard deviation for a Gaussian in continuous action spaces).
Critic (
V
ϕ
V 
ϕ
​
 
): Takes state 
s
s
 as input and outputs an estimate of the state value 
V
(
s
)
V(s)
.
Advantage Estimation: PPO uses the advantage function 
A
(
s
t
,
a
t
)
=
Q
(
s
t
,
a
t
)
−
V
(
s
t
)
A(s 
t
​
 ,a 
t
​
 )=Q(s 
t
​
 ,a 
t
​
 )−V(s 
t
​
 )
.
A common and effective way to estimate the advantage is using Generalized Advantage Estimation (GAE). GAE provides a balance between using just the immediate TD error (
r
t
+
1
+
V
(
s
t
+
1
)
−
V
(
s
t
)
r 
t+1
​
 +V(s 
t+1
​
 )−V(s 
t
​
 )
), which has low variance but high bias, and using the full discounted return from the current state (
R
t
=
∑
k
=
0
∞
γ
k
r
t
+
k
+
1
R 
t
​
 =∑ 
k=0
∞
​
 γ 
k
 r 
t+k+1
​
 
), which has high variance but low bias.
GAE uses a parameter 
λ
λ
 (typically between 0 and 1). 
λ
=
0
λ=0
 gives the immediate TD error, and 
λ
=
1
λ=1
 approximates the Monte Carlo return. The GAE estimate for the advantage at time 
t
t
 is:
A
^
t
G
A
E
(
γ
,
λ
)
=
∑
l
=
0
∞
(
γ
λ
)
l
δ
t
+
l
A
^
  
t
GAE(γ,λ)
​
 =∑ 
l=0
∞
​
 (γλ) 
l
 δ 
t+l
​
 

where 
δ
t
=
r
t
+
γ
V
(
s
t
+
1
)
−
V
(
s
t
)
δ 
t
​
 =r 
t
​
 +γV(s 
t+1
​
 )−V(s 
t
​
 )
 is the TD error. In practice, the sum is truncated to the length of the collected trajectory.
Data Collection (Rollouts): PPO is on-policy. This means data is collected by running the current policy 
π
θ
o
l
d
π 
θ 
old
​
 
​
 
 in the environment for a fixed number of timesteps or episodes. This data (states, actions, rewards, next states, done flags, and importantly, the log probabilities of the chosen actions under 
π
θ
o
l
d
π 
θ 
old
​
 
​
 
) is stored in a buffer.
Optimization Phase: Once a batch of data is collected:
Use the collected rewards and the critic network 
V
ϕ
V 
ϕ
​
 
 (or 
V
ϕ
o
l
d
V 
ϕ 
old
​
 
​
 
) to compute the target values (
R
^
t
R
^
  
t
​
 
) and advantage estimates (
A
^
t
A
^
  
t
​
 
) for all timesteps in the batch, typically using GAE.
Optimize the combined objective function 
L
(
θ
,
ϕ
)
L(θ,ϕ)
 using stochastic gradient descent (SGD) or a variant like Adam. Crucially, the same collected batch of data is typically used for multiple epochs of optimization (hyperparameter 
K
K
 or num_ppo_epochs).
During these 
K
K
 epochs, the advantage estimates 
A
^
t
A
^
  
t
​
 
 and the old policy log probabilities 
log
⁡
π
θ
o
l
d
(
a
t
∣
s
t
)
logπ 
θ 
old
​
 
​
 (a 
t
​
 ∣s 
t
​
 )
 (and thus 
r
t
(
θ
)
r 
t
​
 (θ)
's denominator) are kept fixed, calculated using the policy and value function before this optimization phase started. The numerator 
π
θ
(
a
t
∣
s
t
)
π 
θ
​
 (a 
t
​
 ∣s 
t
​
 )
 and the value predictions 
V
ϕ
(
s
t
)
V 
ϕ
​
 (s 
t
​
 )
 are computed with the current parameters being optimized.
After 
K
K
 epochs, the parameters 
θ
θ
 and 
ϕ
ϕ
 are updated, and this updated policy becomes the 
π
θ
o
l
d
π 
θ 
old
​
 
​
 
 for the next data collection phase.
6. The PPO Algorithm (Simplified Steps)
Initialize policy parameters 
θ
0
θ 
0
​
 
 and value function parameters 
ϕ
0
ϕ 
0
​
 
.
For iteration 
k
=
0
,
1
,
2
,
…
k=0,1,2,…
:
a. Collect a set of trajectories (a batch of timesteps 
T
T
) by running the policy 
π
θ
k
π 
θ 
k
​
 
​
 
 in the environment. Store 
(
s
t
,
a
t
,
r
t
,
s
t
+
1
)
(s 
t
​
 ,a 
t
​
 ,r 
t
​
 ,s 
t+1
​
 )
 and the log probabilities 
log
⁡
π
θ
k
(
a
t
∣
s
t
)
logπ 
θ 
k
​
 
​
 (a 
t
​
 ∣s 
t
​
 )
 for 
t
=
0
,
…
,
T
−
1
t=0,…,T−1
.
b. Compute advantage estimates 
A
^
t
A
^
  
t
​
 
 for all 
t
t
 in the batch using the rewards and the value function 
V
ϕ
k
V 
ϕ 
k
​
 
​
 
 (typically using GAE with parameters 
γ
,
λ
γ,λ
). Compute target values 
R
^
t
R
^
  
t
​
 
 for the value function loss (e.g., 
R
^
t
=
A
^
t
+
V
ϕ
k
(
s
t
)
R
^
  
t
​
 = 
A
^
  
t
​
 +V 
ϕ 
k
​
 
​
 (s 
t
​
 )
).
c. Optimize the policy and value networks for 
K
K
 epochs using the collected batch data:
i. For epoch 
e
=
0
,
…
,
K
−
1
e=0,…,K−1
:
- Shuffle the batch data and split into minibatches.
- For each minibatch:
- Calculate the probability ratio 
r
t
(
θ
)
=
π
θ
(
a
t
∣
s
t
)
π
θ
k
(
a
t
∣
s
t
)
r 
t
​
 (θ)= 
π 
θ 
k
​
 
​
 (a 
t
​
 ∣s 
t
​
 )
π 
θ
​
 (a 
t
​
 ∣s 
t
​
 )
​
 
 for each 
(
s
t
,
a
t
)
(s 
t
​
 ,a 
t
​
 )
 in the minibatch.
- Calculate the clipped surrogate objective 
L
C
L
I
P
(
θ
)
L 
CLIP
 (θ)
 using 
r
t
(
θ
)
r 
t
​
 (θ)
, 
A
^
t
A
^
  
t
​
 
, and 
ϵ
ϵ
.
- Calculate the value function loss 
L
V
F
(
ϕ
)
=
(
V
ϕ
(
s
t
)
−
R
^
t
)
2
L 
VF
 (ϕ)=(V 
ϕ
​
 (s 
t
​
 )− 
R
^
  
t
​
 ) 
2
 
.
- Calculate the entropy 
S
[
π
θ
]
(
s
t
)
S[π 
θ
​
 ](s 
t
​
 )
.
- Form the total loss 
L
(
θ
,
ϕ
)
=
−
L
C
L
I
P
(
θ
)
+
c
1
L
V
F
(
ϕ
)
−
c
2
S
[
π
θ
]
(
s
t
)
L(θ,ϕ)=−L 
CLIP
 (θ)+c 
1
​
 L 
VF
 (ϕ)−c 
2
​
 S[π 
θ
​
 ](s 
t
​
 )
 (note the signs are flipped if minimizing the negative objective).
- Compute gradients of 
L
L
 with respect to 
θ
θ
 and 
ϕ
ϕ
 and update parameters using an optimizer (e.g., Adam).
d. Set 
θ
k
+
1
←
θ
θ 
k+1
​
 ←θ
 and 
ϕ
k
+
1
←
ϕ
ϕ 
k+1
​
 ←ϕ
.
Repeat until convergence or maximum iterations.
7. Hyperparameters
PPO has several important hyperparameters that need tuning:
learning_rate: For the optimizer (e.g., Adam). Often separate learning rates for actor and critic, though commonly shared.
gamma: Discount factor for future rewards.
lambda: GAE parameter (between 0 and 1).
clip_epsilon: The 
ϵ
ϵ
 value for the clipping range 
[
1
−
ϵ
,
1
+
ϵ
]
[1−ϵ,1+ϵ]
. Typically 0.1 or 0.2.
epochs_per_update (or num_ppo_epochs): The number of gradient steps taken on the same batch of data. Typically 3 to 10.
minibatch_size: The size of minibatches used during the optimization epochs.
n_steps or rollout_length: The number of timesteps collected in each data collection phase before performing updates.
entropy_coeff: The weight 
c
2
c 
2
​
 
 for the entropy bonus.
8. Pros and Cons of PPO
Pros:
State-of-the-art Performance: Often achieves performance competitive with or better than TRPO and other complex algorithms on a wide range of tasks.
Simplicity: Significantly simpler to implement than TRPO, using only first-order gradient methods.
Stability: The clipping mechanism provides more stable updates compared to vanilla policy gradient methods.
Compatibility: Easily integrates with neural networks that share parameters between policy and value function, and compatible with exploration techniques like the entropy bonus.
Cons:
Data Efficiency: As an on-policy algorithm, it requires new data collected with the current policy for each major update iteration. This can be less data-efficient than off-policy methods that can reuse older data.
Hyperparameter Sensitivity: While less sensitive than VPG, performance can still depend significantly on the choice of hyperparameters, especially clip_epsilon, learning rates, and epochs_per_update.