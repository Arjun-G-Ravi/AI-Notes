# Initialization

- Initialization in a nn refers to the process of setting the initial values of the model's parameters (weights and biases) before training.
- Proper initialization is critical because it can impact how quickly and effectively a neural network converges during training. 
- Poor initialization can lead to slow convergence or even cause the model to get stuck in poor local minima.
- Improper initialisation can lead to dead neurons

Some common initialization methods are:

## 1. Zero initialization
- All weights are initialized to zero.
- This prevents the model from learning effectively since each neuron will have identical gradients and update in the same direction.

## 2. Random initialization
- Weights are initialized to small random numbers.
- Simply initializing with random values might cause gradients to either vanish or explode, depending on the activation function.

## 3. Xavier (Glorot) Initialization:
- Used with activation functions like sigmoid or tanh.
- The weights are drawn from a distribution with a mean of `0` and variance of `2 / (n_in + n_out)`
- Helps keep the variance of the activations and gradients similar across layers, which leads to faster convergence.
- `W = np.random.randn(n_in, n_out) * sqrt(2 / (n_in + n_out))`

## 4. He Initialization
- Commonly used with ReLU (Rectified Linear Unit) and its variants.
- The weights are drawn from a distribution with a variance of (2/n_in)
- This method compensates for the fact that ReLU can output 0 for half of the inputs, ensuring better propagation of gradients.
- `W = np.random.randn(n_in, n_out) * sqrt(2 / n_in)`