# MLP
They are feedforward fully connected artificial neural networks. They are the most basic NN architecture.

![Alt text](image-5.png)

## General MLP usage tips
- 2 hidden layers are sufficent for most calculations.
- If there are m training data, a 1-hidden-layer NN with m-1 neurons can perfectly predict each training data. (overfitting)
- In general, using the same number of neurons for all hidden layers will suffice. For some datasets, having a large first layer and following it up with smaller layers will lead to better performance as the first layer can learn a lot of lower-level features that can feed into a few higher order features in the subsequent layers.
- Usually, you will get more of a performance boost from adding more layers than adding more neurons in each layer.
- Andrej Karpathy recommends the overfit then regularize approach — “first get a model large enough that it can overfit and then regularize it appropriately.”

# Notes
- Usually we don't count the input layer as layer. So the image shows a 4 layered neural network. -
- The perceptron learning algorithm is an algorithm that works only if the training data is linearly separable
- MLPs are universal approximators - can approximate any function
- 