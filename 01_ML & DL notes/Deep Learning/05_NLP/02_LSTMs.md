
## LSTM 
Long Short-Term Memory networks were specifically designed to address both the exploding and vanishing gradient problems as well as the long-term dependencies issue, making them a significant improvement over vanilla RNNs in these aspects.

LSTM networks have two kinds of memory – short and long term memory. Each LSTM cell has three gates –  the forget gate, the input gate and the output gate.

![Alt text](image-11.png)

In each gate, the sigmoid activation function determines how much of the data is to be remembered.

### Forget gate
This gate decides how much of the data is to be remembered in the long term memory. The forget gate takes in the weighted sum of the input vector from tth and (t-1)th state, and pass them through a sigmoid function. This gives an output between 0 and 1, which will be multiplied with the long term memory. 

### Input gate
It inserts new memory to the long term memory. It takes in the weighted sum of the input vector from tth and (t-1)th state, and pass them through a sigmoid function and a tanh function. Then those two values are multiplied and added to the long term memory.

### Output gate
It gives out the output, derived from the input, long and short term memory which is to be passed to the next cell (or looped back in). It takes in the weighted sum of the input and short term memory and multiplies it with the tanh of the long term memory. This is the output, which is given out, as the short term memory of the next cell(or looped back in) and the y output from the cell.  
Read later: http://colah.github.io/posts/2015-08-Understanding-LSTMs/


 1. Autoencoders
 2. Generative Adversarial Networks (GANs)
 3. Self-Attention Models