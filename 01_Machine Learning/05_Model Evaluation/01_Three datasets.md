# Model’s Assessment
For model evaluation, we create three separate sets of our dataset:
1. Training set – For training the model
2. Validation set/ Dev set – A dataset for optimising the model. The trained model will be tested on this dataset, and its hyperparameters will be adjusted inorder to get high accuracy in this set.
3. Test set – The dataset used exclusively for testing. No improvement should be made to the model based on this set. The test set contains the examples that the learning algorithm has never seen before, so if our model performs well on predicting the labels of the examples from the test set, we say that our model generalizes well.

#### Inference from the assessment
- High varience - A model that performs well on training set, but is bad on dev set. Looks like the model is not generalising well and is overfitting the training set.

- High bias – A model that fits both the same, but is very bad. It is underfitting both dataset.
Note that a model can have both high varience and high bias. This typically happens for higher dimensional models, where it underfits in one dimension and overfits in another.

