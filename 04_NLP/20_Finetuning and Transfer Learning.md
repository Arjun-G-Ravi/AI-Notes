# Fine-tuning and Transfer Learning

# 1. Fine-tuning
Fine-tuning is the process of adjusting the parameters of a pre-trained model to fit a specific task or dataset. The goal is to `adapt the model to the specific task or dataset`, while leveraging the knowledge and features learned from the pre-training process. 

- This lets us take pretrained models good at general things, and make them super good on a domain of interest.
- Fine tuned models can be better than bigger models in a small(fine tuned)domain.
- Typically, `this training will either freeze(generally we dont freeze - we retrain the model) or make only minimal adjustments to the pretrained language model parameters`.

### 1. Classification
To fine tune a model to do classification, `we add a classifier head` to the very end of the model. 

We also add some additional vector to ensure that the model knows that it classification is to be done.
Eg: Adding a [ CLS ] token at the beggining of input, if classification is to be done.

A key difference from what we’ve seen earlier with neural classifiers is that this loss can be used to not only learn the weights of the classifier, but also to update the weights for the pretrained language model itself. In practice, reasonable classification performance is typically achieved with only minimal changes to the language model parameters, often limited to updates over the final few layers of the transformer.

### 2. Pair-wise sequence classification
Another type of problem where we give two sequences and is required to do classification. Eg: Next sentence prediction, entailment prediction

### 3. Sequence Labelling
Label every sequence. Eg: POS tagging

### 4. Span-based language model
It involves selecting a span of text, masking all the words within that span, and then training the model to predict the original words in the span.

# 2. Transfer Learning
Transfer learning uses `a pre-trained model as a feature extractor and trains a new classifier on top of it`. This technique focuses on transferring general knowledge from one domain to another, and `often involves freezing certain layers to retain general features`.