# Sequence models
Lets say that we have a model (say, a RNN) that does machine translation. How do we ensure that the best possible translation is done?

If we seaching for the highest probable word for each translated word by checking the probability for every combination of words, it will be very computationally expensive. Hence we need a faster, approximating algorithm. 

## Greedy Search
Here, we choose the most likely word from the vocabulory for every predicted word. But this wil not work for every sentence, as it only chooses the best one it gets at the moment. A better answer could be a less probable word combination.

## Beam search algorithm
Beam search algorithm is an extension of the more basic greedy search method and is designed to find the most likely sequence of tokens in a probabilistic model, considering a broader range of possibilities. It maintains a "beam width" parameter, which limits the number of candidate sequences to consider at each step. Beam width of one is the greedy algorithm

- Start with an initial sequence and create a set of candidate sequences (the "beam") with a limited size (the beam width).
- At each step, generate possible next tokens for each sequence in the beam. Calculate the probability of each candidate sequence by multiplying token probabilities along the path.
- Keep only the top k sequences (where k is the beam width) based on their probabilities. This step narrows down the search space to prevent exponential growth.
- If any sequence in the beam generates the end token, it's considered a completed sequence.
- Continue generating tokens until a maximum length is reached or no sequences remain.
- Select the highest-scoring completed sequence as the output. This represents the most likely sequence according to the model's probabilities.

