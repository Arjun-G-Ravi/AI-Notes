# Transformers
Transformers take in RNNs(and GRU and LSTMs) with attention model, and compute them in a CNN style of parallel processing. 

## Self Attention
The key innovation of transformers is their self-attention mechanism, which allows them to process input data in parallel rather than sequentially, making them highly scalable and efficient. This self-attention mechanism enables transformers to capture long-range dependencies in data, making them well-suited for tasks involving sequences.

Attention:
Think of it as a mechanism where a model pays attention to different parts of the input sequence when generating an output.
It's like a person reading a sentence and focusing on different words based on their importance in understanding the context.
It's often used in tasks like machine translation, where the model aligns source words with target words to form translations.

Self-Attention (Scaled Dot-Product Attention):
Self-attention, in the context of transformers, is a specific type of attention mechanism.
In self-attention, a model looks at different words within the same input sequence to understand how they relate to each other.
It's like a person reading a sentence and understanding the relationships between different words in that sentence without any external context.
Transformers use self-attention extensively to build representations of words or tokens in a sequence based on their relationships with other words or tokens in the same sequence.
In self attention,  the word embedding is formed with relation to the input text. But for normal attention, it is not so
Self-attention, sometimes referred to as scaled dot-product attention, is a specific type of attention mechanism used within transformers.

In a transformer, the attention for each word contains three vectors:
    - query: Lets you ask question about the word. 
    - key: Looks at all the words and gives the most relevent answer w.r.t the query
    - value: Gives an embedding of the word, w.r.t the keys. This type of adaptive embedding is vastly superior to raw word embedding.

## Multi-headed attention
This is the self-attention running in a for loop, parallely. At each loop, a different query is asked. 

For eg: To translate Jane visits Africa in September
    - Query1: What with Africa?  # High attention to visits
    - Query2: When visit?  # High attention to September
    - Query3: Who?  # Jane
    - ...
    - ....h heads
![Alt text](<Screenshot from 2023-11-08 21-14-51.png>)


The concatenation of the representation of all the heads is used for final prediction.


# The transformer Architecture

![Alt text](<Screenshot from 2023-11-08 21-23-09.png>)

There are certain things that can vastly improve the performance of transformer models

## 1. Positional Encodings
The position of the words can play a major role in its meaning. So we encode the postion of the words also. Instead of directly adding it, we encode it as sine and cosine wave - probably for performance.

![Alt text](<Screenshot from 2023-11-08 21-33-22.png>)

## 2. Residual Networks
Just like resnet, so that transformers will remember better.

## 3. Batch normalisation
For faster convergence.

Thus the transformers model is:

![Alt text](<Screenshot from 2023-11-08 21-38-39.png>)

![Alt text](1_BHzGVskWGS_3jEcYYi6miQ.png)