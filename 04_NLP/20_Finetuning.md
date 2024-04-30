# Fine-tuning
Fine-tuning is the process of adjusting the parameters of a pre-trained model to fit a specific task or dataset. The goal is to `adapt the model to the specific task or dataset`, while leveraging the knowledge and features learned from the pre-training process. Typically, this training will either freeze or make only `minimal adjustments to the pretrained language model parameters`.

- This lets us take pretrained models good at general things, and make them super good on a domain of interest.

# Classification
To fine tune a model to do classification, `we add a classifier head` to the very end of the model. We also add some prompt to ensure that the model knows that it classification is to be done.
Eg: Adding a [ CLS ] token at the beggining of input, if classification is to be done.

A key difference from what we’ve seen earlier with neural classifiers is that this loss can be used to not only learn the weights of the classifier, but also to update the weights for the pretrained language model itself. In practice, reasonable classification performance is typically achieved with only minimal changes to the language model parameters, often limited to updates over the final few layers of the transformer.

