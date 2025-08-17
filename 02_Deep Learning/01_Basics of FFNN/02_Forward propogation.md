# Forward Propogation

As the input matrix is passed from one layer to another, it is matmuled by the weight matrix and added to bias matrix. 
The whole thing is passed to an activation function before being passed on to the next layer. 
The activation function determines if the neuron is activated for the next layer. 

For each layer L ,if g is the activation function,

            f(X) = g( W.X + b )

So, the whole NN would look like: ```fnn(X) = f1(f2(f3(X)))``` 

i.e, a NN is a nested function where each layer acts as a function.

This whole process where the input propogates through the different layers to the output layer to perform inference is called forward propogation. 
Forward pass happen during training and inference phase.

If the activation function  of the last unit is 
- Linear:  the neural network is a regression model. 
- Sigmoid: It is a binary classification model.
- Softmax: Multi-class classification