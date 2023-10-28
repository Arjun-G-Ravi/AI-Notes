# Sequence models
Lets say that we have a model (say, a RNN) that does machine translation. How do we ensure that the best possible translation is done?

## 1. Searching every possibility (in vocabulory)
If we seaching for the highest probable word for each translated word by checking the probability for every combination of words, it will be very computationally expensive. Hence we need a faster, approximating algorithm. 

## 2. Greedy Search
Here, we choose the most likely word from the vocabulory for every predicted word. But this wil not work for every sentence, as it only chooses the best one it gets at the moment. A better answer could be a less probable word combination.

## 3. Beam search algorithm
Beam search algorithm is an extension of the more basic greedy search method and is designed to find the most likely sequence of tokens in a probabilistic model, considering a broader range of possibilities by using a heuristic. It maintains a "beam width" parameter, which limits the number of candidate sequences to consider at each step. Beam width of one is the greedy algorithm

![Alt text](<Screenshot from 2023-10-28 20-35-08.png>)

- Start with an initial sequence and create a set of candidate sequences (the "beam") with a limited size (the beam width).
- At each step, generate possible next tokens for each sequence in the beam. Calculate the probability of each candidate sequence by multiplying token probabilities along the path.
- Keep only the top k sequences (where k is the beam width) based on their probabilities. This step narrows down the search space to prevent exponential growth.
- If any sequence in the beam generates the end token, it's considered a completed sequence.
- Continue generating tokens until a maximum length is reached or no sequences remain.
- Select the highest-scoring completed sequence as the output. This represents the most likely sequence according to the model's probabilities.

Beam width is BIG: Better results, more RAM, slower 
Beam width is SMALL: Worse results, less RAM, faster


## 4. Upgrades to beam search

**Length normalisation**: For finding probability of a sentence, we find the probability for each word given the earlier ones. This can lead to floating point underflows. Inorder to prevent this, we take the log of the probabilities and add them up. 

But all these algos will prefer shorter sentence over longer ones. So, normalise the output by dividing by the length of the sentence.

![Alt text](<Screenshot from 2023-10-28 20-30-51.png>)

## 5. Error Analysis
To figure out if we have faulty RNN or faulty (beam) search algorithm.
![Alt text](<Screenshot from 2023-10-28 20-40-26.png>)

## 6. Bleu Score

BLEU (Bilingual Evaluation Understudy) is a metric used to evaluate the quality of machine-generated translations, primarily in the context of machine translation tasks. It was developed as a way to measure the similarity between a machine-generated translation and one or more human reference translations.
The BLEU score is a number between 0 and 1, with 1 being a perfect match to the human reference translations. It measures the precision of the machine-generated translation by comparing the n-grams (contiguous sequences of words or characters) in the generated text to those in the reference text. The more n-grams that match, the higher the BLEU score.

![Alt text](<Screenshot from 2023-10-28 20-58-18.png>)
It is used in NLP situations where multiple answers can be correct like translation. Speech-to-text shouldnot use bleu score, as we always expect a one-on-one correct answer.

## 7. Attention models

