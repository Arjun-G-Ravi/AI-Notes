## General MLP usage techniques
- 2 hidden layers are sufficent for most calculations.
- If there are m training data, a 1-hidden-layer NN with m-1 neurons can perfectly predict each training data. (overfitting)
- In general, using the same number of neurons for all hidden layers will suffice. For some datasets, having a large first layer and following it up with smaller layers will lead to better performance as the first layer can learn a lot of lower-level features that can feed into a few higher order features in the subsequent layers.
- Usually, you will get more of a performance boost from adding more layers than adding more neurons in each layer.
- Andrej Karpathy recommends the overfit then regularize approach — “first get a model large enough that it can overfit and then regularize it appropriately.”
