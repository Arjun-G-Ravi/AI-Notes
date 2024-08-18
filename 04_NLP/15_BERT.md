# BERT
BERT (Bidirectional Encoder Representations from Transformers) is a language model developed by Google in 2018.

The key innovation of BERT is its use of a `bidirectional transformer architecture`, which allows the model to capture both the forward and backward contextual relationships between words in the text. This allows the model to better understand the meaning of the text and make more accurate predictions.

- It is an `encoder only model`
- BERT is supposed to demonstrate the importance of bidirectional pre-training for language representations.
- By adding one more layer on bert and fine-tuning, BERT could be used for even text generation. But it can't be used for Causal text generation in an autoregressive manner(You'd need models like GPT for that). 

![alt text](<Screenshot from 2024-04-28 14-19-22.png>)

# Training
BERT has two stages in its training.
1. Pre-training
2. Fine-tuning

## Pretraining
There are two ways in which BERT is pretrained.

### 1. Masked LM  
During pre-training, BERT randomly masks out a fixed percentage of random words. Then the model is trained to predict it.

Although this allows us to obtain a bidirectional pre-trained model, a downside is that we are creating a mismatch between pre-training and fine-tuning, since the [ MASK ] token does not appear during fine-tuning. To mitigate this, whenever we are supposed to replace a word, we:
1. replace by [ MASK ] 80% of time 
2. replace by random token 10% of time
3. not at all replaced 10% of time

### 2. Next Sentence Prediction (NSP)
BERT is trained to preict if two sentences come after the other. This will let BERT learn about the relationship between two sentences.

![alt text](<Screenshot from 2024-04-28 14-13-30.png>)

## Fine tuning
Thus it will have a pretty good understanding of the language. Then it is fine tuned on the text it is supposed to excel such as text completion, masked-word prediction, classification, named entitiy recognition, etc.
