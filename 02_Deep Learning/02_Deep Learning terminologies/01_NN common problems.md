# Exploding and Vanishing gradients

Exploding and vanishing gradients are issues that can occur during the training of neural networks, particularly those with many layers. These problems are related to the way gradients are propagated backward through the network during the backpropagation process. It is vastly prevalent in RNNs.

- **Exploding Gradients:** When gradients grow exponentially as they are propagated backward through the layers of a deep neural network, it's referred to as the "exploding gradients" problem. As the gradients become extremely large, parameter updates can also become very large, causing the network's parameters to change significantly in each iteration. This can lead to instability in training, making it difficult for the network to converge to a good solution.

- **Vanishing Gradients:** This often happens when the network has many layers, particularly in networks with activation functions that squash their inputs. As gradients become smaller and smaller, the updates to the parameters become insignificant, and the network learns at an extremely slow pace. This can lead to early layers of the network not learning effectively, resulting in poor overall performance.
One way to reduce this problem is to initialise the weights with a varience of 1/n (or 2/n).

# Plateauing during Optimisation
Most of the 'derivative = 0' points in a high dimensional function are saddle points, not local minima. So getting stuck in a local minima is not a common problem. But plateuing is.
