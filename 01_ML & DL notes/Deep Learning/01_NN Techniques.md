# TECHNIQUES TO BE USED WHEN NEURAL NETWORKING

## 1. Gradient Checking
It is a method for checking if gradient calculation is accurate or not. It can be used to verify if backpropogation implementation is correct or not.

## 2. Exploding and Vanishing gradients

Exploding and vanishing gradients are issues that can occur during the training of neural networks, particularly those with many layers. These problems are related to the way gradients are propagated backward through the network during the backpropagation process. It is vastly prevalent in RNNs.

**Exploding Gradients:** When gradients grow exponentially as they are propagated backward through the layers of a deep neural network, it's referred to as the "exploding gradients" problem. As the gradients become extremely large, parameter updates can also become very large, causing the network's parameters to change significantly in each iteration. This can lead to instability in training, making it difficult for the network to converge to a good solution.

**Vanishing Gradients:** This often happens when the network has many layers, particularly in networks with activation functions that squash their inputs. As gradients become smaller and smaller, the updates to the parameters become insignificant, and the network learns at an extremely slow pace. This can lead to early layers of the network not learning effectively, resulting in poor overall performance.

One way to reduce this problem is to initialise the weights with a varience of 1/n (or 2/n).

## 3. Regularisation in Neural Networks
L2 Regularisation can be implemented in nn, just like in other ML algorithms by adding a regularising term. 

Another powerful regularisation technique for NN is dropout regularisation. Dropout is a method to combat overfitting by randomly deactivating (or "dropping out") a fraction of neurons during each training iteration.

## 4. Normalisation
Normalisation is the process of converting a dataset which has a high varience to a number between (0,1). This can lead to a massive improvement in the performance of the nn.

![Alt text](<Screenshot from 2023-10-11 20-38-12.png>)

## 5. Initialising
Initialise 
 - weights via Xavier initialisation if you are using tanh function. 
 - weights by sqrt(2/n^(l-1)) if using ReLu
 - bias by zero 

## 6. Gradient checking
Gradient checking is a technique used to verify the correctness of the gradients computed during the training of machine learning models, especially in the context of gradient-based optimization algorithms like stochastic gradient descent (SGD). It helps ensure that the analytical or numerical gradients calculated for the model's parameters (weights and biases) are consistent with the gradients computed using a finite difference approximation.

**Gradient Checking Algorithm**
```
1. ε is a very small value.

2. For each parameter (weight or bias) in the model:
   a. Compute the gradient normally. (to verify)
   b. Calculate the gradient for that parameter by taking the average of gradient calculated after
        - adding ε to parameter 
        - subtracting ε from parameter 
   c. Calculate the absolute difference between the two gradients

3. Repeat step 2 for all the parameters in your model.

4. If the absolute difference is smaller than epsilon, consider the gradient calculation for that parameter to be correct. Otherwise, there is some mistake.
5. After checking all parameters, if all gradients are correct (i.e., their absolute differences with numerical gradients are smaller than epsilon), you can be more confident that your gradient calculations are accurate.
```

## 7. Batching the dataset
Instead of training the whole dataset in one go, we split up dataset as batches. This vastly speeds up the training process, as each epoch takes way less time. After this, we can implement mini batch gradient descent for optimisation.

## 8. Exponentially weighted average
Exponentially weighted average is a statistical technique that give more weight to recent data points while diminishing the influence of older data points. This is used in ML to update paramters based on influence from earlier parameters.

y(t) = beta*y(t-1) + (1-beta)*f(x)

Bias correction can be implemented in this to make this more accurate.

## 9. Gradient Descent with momentum
The basic idea is to compute an exponentially weighted average of your gradients, and then use that gradient to update your weights instead.

This is helpful if the gradient has to go slow in one direction and fast in the other.So, we can use a larger lr, and be fine with it. It can be seen in the diagram below.
![Alt text](<Screenshot from 2023-10-12 21-11-00.png>)

## 10. RMSprop
Just like Grad desc with moementum, with a small algorithmic change.
RMSprop, which stands for Root Mean Square Propagation, is an optimization algorithm commonly used in training machine learning models, particularly deep neural networks.The primary goal of RMSprop is to adapt the learning rates for each parameter during training, making it suitable for non-stationary and ill-conditioned problems. It helps to converge faster and reach better solutions by scaling the learning rates based on the historical gradient information.

![Alt text](<Screenshot from 2023-10-12 21-24-45.png>)

## 11. Adam Optimisation algorithm
The Adam (Adaptive Moment Estimation) optimization algorithm is basically taking momentum and RMSprop, and putting them together. Generally, bias correction and mini-batching is also done in Adam. It is way superrior to gradient descent for optimisation purposes.

![Alt text](<Screenshot from 2023-10-13 06-35-25.png>)

## 12. Learning Rate Decay

One of the things that might help speed up your learning algorithm is to slowly reduce your learning rate over time. This is called learning rate decay, and can be implemented as:
![Alt text](<Screenshot from 2023-10-13 06-39-52.png>)

This works, because we might want a large lr at the start, and smaller ones as we get to the end of the optimisation process.

![Alt text](<Screenshot from 2023-10-13 06-41-27.png>)

## 13. Local Minima
Most of the 'dertivative = 0' points in a high dimensional function are saddle points, not local minima. So getting stuck in a local minima is not a common problem. But plateuing is.

## 14. Batch normalisation
Normalising each layers of the nn, before applying the activation function.