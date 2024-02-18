# Initialisation
For best performance, initialise 
 - weights via Xavier initialisation if you are using tanh function. 
 - weights by sqrt(2/n^(l-1)) if using ReLu
 - bias by zero 

# Normalisation
Normalisation is the process of converting a dataset which has a high varience to a number between (0,1). Just like for other ML algorithms, this can lead to a massive improvement in the performance of the nn.

![Alt text](<Screenshot from 2023-10-11 20-38-12.png>)

# Regularisation
L2 Regularisation can be implemented in nn, just like in other ML algorithms by adding a regularising term. 

In neural networks, besides L0 and L2 regularization, you can use neural network specific regularizers: dropout, early stopping, and batch-normalization.

- Dropout: Each time you run a training example through the network, you temporarily exclude at random some units from the computation. The higher the percentage of units excluded the higher the regularization effect.
  
- Early stopping: It works by monitoring a model's performance on a held-out validation set, and stopping training when the model's performance on the validation set starts to degrade.
  
- Batch normalization (which rather has to be called batch standardization) is a technique that consists of standardizing the outputs of each layer before the units of the subsequent layer receive them as input. In practice, batch normalization results in faster and more stable training, as well as some regularization effect.

# Gradient checking
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

# Batching the dataset
Instead of training the whole dataset in one go, we split up dataset as batches. This vastly speeds up the training process, as each epoch takes way less time. After this, we can implement mini batch gradient descent for optimisation.`