# One-hot word embedding
In a one-hot representation, each word in the vocabulary is uniquely encoded as a binary vector where all values are zero except for one, which is set to one. 
One disadvantage of this is that it treats a word as itself, and doesn't let an algorithm generalize the meaning of one word to another.
This is because the inner product between any two vectors in this representation is zero.
Inner product measures how much of vector A lies in the direction of vector B - the alignment of two vectors.

# Word Embeddings
Word embeddings are distributed representations of words in a vector space, where words with similar meanings are represented by similar vectors. These vector representations are used to capture the semantic and syntactic relationships between words and are a fundamental concept in NLP. These embeddings can be learned by eating up a large corpus of text data.
![Alt text](<Screenshot from 2023-10-20 20-29-14.png>)
Visualising this on a graph will reveal that similar items will be grouped together.

## Featurised Representation of Word embeddings
Featurized representations of word embeddings, often referred to as feature engineering, involve extracting or creating additional features from word embeddings to enhance their utility for specific NLP tasks.

## Extracting relationships from word embeddings
Man : Woman  =  King : ?

We can solve this by subtracting embeddings of (Man and Woman) and finding a embedding that gives the similar result with King.
![Alt text](<Screenshot from 2023-10-20 21-00-18.png>)

 This similarity is usually done by cosine similarity. 
![Alt text](<Screenshot from 2023-10-20 21-07-46.png>)

## Embedding Matrix
It is a matrix that contains the word embeddings for all the words in a vocabulary. To get the word embeddings of a word, we matmul this matrix with the one hot encoding vector of the word, whose word embedding is needed.