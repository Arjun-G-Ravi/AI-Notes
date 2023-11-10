# Transformers
Transformers, a revolutionary neural network architecture, introduce a self-attention mechanism that enables the model to weigh the importance of different elements in a sequence dynamically. Incorporating positional encoding, transformers capture the sequential order of input data. The architecture comprises an encoder-decoder structure, where the encoder processes input information, and the decoder generates output. Multi-head attention enhances the model's ability to capture diverse relationships by employing parallel attention mechanisms. Layer normalization and residual connections contribute to stable and effective training. Feedforward neural networks further refine information extracted through attention mechanisms. Notably, transformers exhibit scalability, efficiently handling long-range dependencies and large datasets, making them versatile for a range of applications in natural language processing and beyond.

In short,transformer architecture can be summarised as:

    1. Input Representation:
        Embedding: Convert input words into vectors (embeddings).

    2. Positional Encoding:
        Add Positional Information: Since Transformers don't inherently understand the order of words in a sequence, positional encodings are added to the input embeddings to give the model information about the position of each word.

    3. Encoder: The input sequence is passed through multiple identical layers in the encoder. Each layer has two sub-layers:

        Self-Attention Mechanism: Allows the model to weigh different parts of the input sequence differently when making predictions.
        Feedforward Neural Network: Applies a set of transformations to the outputs of the self-attention layer.

    4. Decoder: Similar to the encoder but with an additional layer:
        Masked Self-Attention Mechanism: Ensures that each position in the decoder can only attend to positions before it. This prevents information flow from future tokens during training.
    
    5. Attention Mechanism:
        Scaled Dot-Product Attention: Calculates attention scores by taking a weighted sum of values, where the weights are determined by the compatibility (dot product) between a query and keys.

    6. Layer Normalization and Residual Connections:
        Normalization: Each sub-layer output is normalized to stabilize and speed up training.
        Residual Connections: Original inputs to a sub-layer are combined with its output, helping with the flow of gradients during training.

    7. Multi-Head Attention:
        Parallel Attention Mechanisms: The attention mechanism is applied multiple times in parallel, each with different learned weights. The outputs are then concatenated and linearly transformed.
    
    8. Final Linear and Softmax Layers:
    The output of the decoder is transformed into the final output vocabulary size through a linear layer. Softmax is applied to get probabilities.

## Self Attention
The key innovation of transformers is their self-attention mechanism, which allows them to process input data in parallel rather than sequentially, making them highly scalable and efficient. This self-attention mechanism enables transformers to capture long-range dependencies in data, making them well-suited for tasks involving sequences.

### Attention:
- Think of it as a mechanism where a model pays attention to different parts of the input sequence when generating an output.
- It's like a person reading a sentence and focusing on different words based on their importance in understanding the context.
- It's often used in tasks like machine translation, where the model aligns source words with target words to form translations.

### Self-Attention (Scaled Dot-Product Attention):
- Self-attention, sometimes referred to as scaled dot-product attention, is a specific type of attention mechanism used within transformers.
- In self-attention, a model looks at different words within the same input sequence to understand how they relate to each other.
- It's like a person reading a sentence and understanding the relationships between different words in that sentence without any external context.
- Transformers use self-attention extensively to build representations of words or tokens in a sequence based on their relationships with other words or tokens in the same sequence.

##### The HUGE difference
In self attention, the word embedding is formed with relation to the input text. But for normal attention, it is not so. ie,
For the following senteces, apple has the same vector representation in attention mechanism(like using word2vec), but very different representation if self attention is used.
 - Steve Jobs is the CEO of apple.
 - An apple fell over Newton's head.

### Query, Key, Value system for attention
The Query, Key, Value (QKV) system is a fundamental component of the attention mechanism used in transformers. In this system, when processing a sequence of input data, each element (e.g., word) is associated with three vectors: a Query vector (Q), a Key vector (K), and a Value vector (V). Here's a brief overview of their roles:

1. Query (Q): This vector represents the element that is used to inquire about the other elements in the sequence. In the context of attention mechanisms, the query is used to calculate the attention scores indicating how much focus each element should receive.
2. Key (K): The key vector is associated with the element being considered for attention. The key helps determine the relevance of this element to the query. The dot product of the query and key vectors is used to calculate the attention scores.
3. Value (V): The value vector contains information about the element being considered. The attention scores (derived from the query-key interaction) are used to weight the values. The final weighted sum of values forms the output of the attention mechanism for that particular element.

The QKV system is crucial in the attention mechanism's ability to selectively focus on different parts of the input sequence, allowing transformers to capture complex relationships and dependencies within the data. This mechanism is typically used in multiple heads (multi-head attention) to enhance the model's capacity to learn diverse patterns and representations.

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
The most basic part of the transformers is shown here. 
![Alt text](<Screenshot from 2023-11-08 21-23-09.png>)

There are certain things that can vastly improve the performance of transformer models

## 1. Positional Encodings
The position of the words can play a major role in its meaning. So we encode the postion of the words also. This will shift the word in the vector space along a particular dimension, closer to other words with the same index. This will let the model have a better understanding of the context. This shift should not be too large, or else the positional similarity will overwrite the semantics similarity with other words.So, we encode the position as sine and cosine wave .

![Alt text](<Screenshot from 2023-11-08 21-33-22.png>)

## 2. Residual Networks
Just like resnet, so that transformers will remember better.

## 3. Batch normalisation
For faster convergence.

# Transformers
![Alt text](<Screenshot from 2023-11-08 21-38-39.png>)

![Alt text](1_BHzGVskWGS_3jEcYYi6miQ.png)


# Credits

1. Andrew Ng deep learning
2. https://www.youtube.com/watch?v=zxQyTK8quyY&t=1s&ab_channel=StatQuestwithJoshStarmer
3. https://www.youtube.com/watch?v=4Bdc55j80l8&t=1s&ab_channel=TheA.I.Hacker-MichaelPhi
4. https://www.youtube.com/watch?v=kCc8FmEb1nY&t=4s&ab_channel=AndrejKarpathy
5. 