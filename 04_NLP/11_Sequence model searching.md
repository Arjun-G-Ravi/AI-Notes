# Autoregressive Generation 
Decoding from a language model in a left-to-right manner and thus repeatedly choosing the next word conditioned on our previous choices is called `autoregressive generation` or `Causal LM generation.` Here, the model is trained to generate text by considering the dependencies and relationships between the words generated before.

# Sequence model searching
Selecting the best word form softmax layer for autoregression is called sequcence model searching or decoding. It is essential to ensure that the best word is selected. There are many methods to do so:

## Greedy search 
At the softmax layer, the most likely word is chosen given the context. This is called greedy decoding because it makes a locally optimal choice at each time step, even though that maynot be the case in the long run.

- But we dont use it as it gives in a very repetitive answer
- So we use other sampling techniques like beam search.

## Probabilistic Sampling
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

## Beam search algorithm
Beam search algorithm is an extension of the more basic greedy search method and is designed to find the most likely sequence of tokens in a probabilistic model, considering a broader range of possibilities by using a heuristic. It maintains a "beam width" parameter, which limits the number of candidate sequences to consider at each step. Beam width of one is the greedy algorithm

![Alt text](<Screenshot from 2023-10-28 20-35-08.png>)

- Start with an initial sequence and create a set of candidate sequences (the "beam") with a limited size (the beam width).
- At each step, generate possible next tokens for each sequence in the beam. Calculate the probability of each candidate sequence by multiplying token probabilities along the path.
- Keep only the top k sequences (where k is the beam width) based on their probabilities. This step narrows down the search space to prevent exponential growth.
- If any sequence in the beam generates the end token, it's considered a completed sequence.
- Continue generating tokens until a maximum length is reached or no sequences remain.
- Select the highest-scoring completed sequence as the output. This represents the most likely sequence according to the model's probabilities.

```
Beam width is BIG: Better results, more RAM, slower 
Beam width is SMALL: Worse results, less RAM, faster
```

**Length normalisation**: For finding probability of a sentence, we find the probability for each word given the earlier ones. This can lead to floating point underflows. Inorder to prevent this, we take the log of the probabilities and add them up. `But beam search will prefer shorter sentence over longer ones. So, normalise the output by dividing by the length of the sentence.`

![Alt text](<Screenshot from 2023-10-28 20-30-51.png>)