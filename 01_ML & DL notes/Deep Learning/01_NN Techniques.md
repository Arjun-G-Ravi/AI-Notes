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

   