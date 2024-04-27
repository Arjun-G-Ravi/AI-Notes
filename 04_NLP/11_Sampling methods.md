# Autoregressive Generation 
Decoding from a language model in a left-to-right manner and thus repeatedly choosing the next word conditioned on our previous choices is called `autoregressive generation` or `Causal LM generation.` Here, the model is trained to generate text by considering the dependencies and relationships between the words generated before.

# Decoding
Selecting the best word form softmax layer for autoregression is called decoding. It is essential to ensure that the best word is selected. There are many methods to do so:

## Greedy decoding
At the softmax layer, the most likely word is chosen given the context. This is called greedy decoding because it makes a locally optimal choice at each time step, even though that maynot be the case in the long run.

- But we dont use it as it gives in a very repetitive answer
- So we use other sampling techniques like beam search.

## Sampling
This refers to the process of selecting words according to the probability from softmax layer.

## Top-k sampling

Top-k sampling is a simple generalization of greedy decoding. Instead of choosing the single most probable word to generate, we first truncate the distribution to the `top k most likely words`, renormalize to produce a legitimate probability distribution, and then randomly sample from within these k words according to their renormalized probabilities

## Top-p sampling(nucleus sampling)
It keeps not the top k words, but the `top p percent of the probability mass`. The goal is to truncate the distribution to remove the very unlikely words. 

## Temperature sampling
In temperature sampling, we don’t truncate the distribution, but instead reshape the distribution of the softmax with the help of a temperature. Higher values make the distribution more and more uniform.

![alt text](<Screenshot from 2024-04-27 15-43-00.png>)

Temperature:
- Closer to 0: Stable and less creative
- Closer to 1: Unstable and more creative.
- Higher than 1: Very creative, maybe even stupid because of the randomness.
