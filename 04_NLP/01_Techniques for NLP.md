# NLP Techniques

## 1. Teacher Forcing
Teacher forcing is a common training strategy for recurrent neural networks (RNNs) and other sequence-to-sequence models. In teacher forcing, the model is trained using the true previous inputs (or "history sequence") rather than its own previous outputs. This allows the model to learn the correct mapping between input sequences and output sequences, and can lead to faster and more stable convergence during training.

However, teacher forcing can also lead to a discrepancy between training and inference, as the model is not exposed to its own errors during training. This can result in poor performance at inference time, especially when the model is used to generate long sequences. To solve that we use professor forcing.

## 2. Professor Forcing/ Scheule sampling
For "professor forcing" or "scheduled sampling", the model is trained using a mixture of true previous inputs and its own previous outputs. This can help the model to learn to recover from its own errors and improve its performance at inference time.

## 3. Weight Tying
Weight tying is a technique used in some neural network architectures to reduce the number of parameters and improve the generalization performance of the model. In weight tying, the weights of two or more layers in the network are constrained to be identical, so that they share the same set of parameters. Often used in encoder-decoder systems.
