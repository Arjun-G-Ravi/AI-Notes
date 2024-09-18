# NLP Techniques

## 1. Teacher Forcing
Teacher forcing is a common training strategy for recurrent neural networks (RNNs) and other sequence-to-sequence models. In teacher forcing, the model is trained using the true previous inputs (or "history sequence") rather than its own previous outputs. This allows the model to learn the correct mapping between input sequences and output sequences, and can lead to faster and more stable convergence during training.

However, teacher forcing can also lead to a discrepancy between training and inference, as the model is not exposed to its own errors during training. This can result in poor performance at inference time, especially when the model is used to generate long sequences. To solve that we use professor forcing.

## 2. Professor Forcing/ Scheule sampling
For "professor forcing" or "scheduled sampling", the model is trained using a mixture of true previous inputs and its own previous outputs. This can help the model to learn to recover from its own errors and improve its performance at inference time.

## 3. Weight Tying
Weight tying is a technique used in some neural network architectures to reduce the number of parameters and improve the generalization performance of the model. In weight tying, the weights of two or more layers in the network are constrained to be identical, so that they share the same set of parameters. Often used in encoder-decoder systems.

## 4. Negative Sampling
Negative sampling is a technique used during the training of word embedding models, such as Skip-gram, to make the training process more efficient and manageable. During training, we choose the correct context and word pair, and many other 'wrong'(negative) words with the context. Then we train a supervised learning algorithm with the dataset. 

![Alt text](<Screenshot from 2023-10-25 21-33-19.png>)

Thus instead of training a whole softmax layer for predicting for the whole vocabulory, we train on multiple k-1 number of negative sample and 1 positive sample. This leads to lowered computational cost, with comparable performance. 

Thus one 10K-way softmax -> 10K k-way binary classification.

The selection of the negative samples is not random, but based on a huristic value.

## 5. Logit Lens

The Logit Lens is a method that allows you to take any vector from any layer of the transformer model and pretend that it's the pre-final embedding.
Then, you multiply it by the unembedding layer to get logits, and finally, you compute a softmax to see the distribution over words that that vector might be representing.


- The Logit Lens is specifically designed for transformer-based models. It lets us understand the understanding of the diffrerent layers of a model.

- The model wasn't trained to produce these internal representations, so the Logit Lens may not always work perfectly. However, it can still be a useful trick for gaining insights into the model's behavior.