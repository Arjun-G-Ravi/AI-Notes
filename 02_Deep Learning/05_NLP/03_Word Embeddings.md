# One-hot word embedding
In a one-hot representation, each word in the vocabulary is uniquely encoded as a binary vector where all values are zero except for one, which is set to one. 
One disadvantage of this is that it treats a word as itself, and doesn't let an algorithm generalize the meaning of one word to another.
This is because the inner product between any two vectors in this representation is zero.
Inner product measures how much of vector A lies in the direction of vector B - the alignment of two vectors.

# Word Embeddings
Word embeddings are distributed representations of words in a vector space, where words with similar meanings are represented by similar vectors. These vector representations are used to capture the semantic and syntactic relationships between words and are a fundamental concept in NLP. These embeddings can be learned by eating up a large corpus of text data.

![Alt text](<Screenshot from 2023-10-20 20-29-14.png>)
Visualising this on an n-dimensional graph will reveal that similar items will be grouped together.

## Feature Enginnering
Featurized representations of word embeddings, often referred to as feature engineering, involve extracting or creating additional features from word embeddings to enhance their utility for specific NLP tasks.

## Extracting relationships from word embeddings
Man : Woman  =  King : ?

We can solve this by subtracting embeddings of (Man and Woman) and finding a embedding that gives the similar result with King.

![Alt text](<Screenshot from 2023-10-20 21-00-18.png>)

 This similarity is usually done by cosine similarity. 
![Alt text](<Screenshot from 2023-10-20 21-07-46.png>)

## The embedding Matrix
It is a matrix that contains the word embeddings for all the words in a vocabulary. To get the word embeddings of a word, we matmul the embedding matrix with the one hot encoding vector of the word, whose word embedding is needed.

## Skip gram - a Word2Vec embedding
Skip-gram is a type of word embedding model used in natural language processing and natural language understanding tasks. Skip-gram is part of the word2vec family of models, which aims to capture the semantic relationships between words in continuous vector spaces.

- The skip-gram model starts by being fed a large dataset of text. 

- As the model processes the text, it uses a sliding context window that moves along the text. This context window is like a spotlight that focuses on a small portion of the text at a time.

- At each position where the context window stops, the model selects a single target word from the center of the window. This word is the one the model wants to understand better and create an embedding for.

- The model's goal is to predict the surrounding words within the context window. These surrounding words are referred to as "context words." The model is trained to guess which words are likely to appear in the context of the chosen target word.

- Training Objective: The training process involves adjusting the model's parameters (weights) to maximize the likelihood that it predicts the context words correctly given the target word. In essence, it learns to understand the relationships between words by observing how they co-occur in the training data.

- Word Embeddings: The result of this training process is a set of word embeddings. These embeddings capture the meaning and context of words based on their co-occurrence patterns in the text.

## Negative Sampling
Negative sampling is a technique used during the training of word embedding models, such as Skip-gram, to make the training process more efficient and manageable. During training, we choose the correct context and word pair, and many other 'wrong'(negative) words with the context. Then we train a supervised learning algorithm with the dataset. 

![Alt text](<Screenshot from 2023-10-25 21-33-19.png>)

Thus instead of training a whole softmax layer for predicting for the whole vocabulory, we train on multiple k-1 number of negative sample and 1 positive sample. This leads to lowered computational cost, with comparable performance. 

Thus one 10K-way softmax -> 10K k-way binary classification.

The selection of the negative samples is not random, but based on a huristic value.

## GloVe (Global vectors for word representations)

GloVe is a word embedding model that works by learning continuous vector representations for words. GloVe is designed to capture semantic and syntactic relationships between words based on their co-occurrence patterns in a large corpus of text. 