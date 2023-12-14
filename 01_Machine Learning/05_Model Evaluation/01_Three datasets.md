# Model’s Assessment
For model evaluation, we create three separate sets of our dataset:
1. Training set – For training the model
2. Validation set/ Dev set – A dataset for optimising the model. The trained model will be tested on this dataset, and its hyperparameters (and other things) will be updated inorder to get high accuracy in this set.
3. Test set – The dataset used exclusively for testing. No improvement should be made to the model based on this set.The test set contains the examples that the learning algorithm has never seen before, so if our model performs well on predicting the labels of the examples from the test set, we say that our model generalizes well or, simply, that it’s good.

#### Inference from the assessment
- High varience - A model that performs well on training set, but is bad on dev set. Looks like the model is not generalising well and is overfitting the training set.

- High bias – A model that fits both the same, but is very bad. It is underfitting both dataset.
Note that a model can have both high varience and high bias. This typically happens for higher dimensional models, where it underfits in one dimension and overfits in another.


       3. Hyperparameter Tuning
Hyperparameters are variables that are not optimized by the learning algorithm itself. The data analyst has to “tune” hyperparameters by experimentally finding the best combination of values, one per hyperparameter.
One method is grid search, but trying all combinations of hyperparameters, especially if there are more than a couple of them, could be time-consuming. 
There are more efficient techniques, such as random search and Bayesian hyperparameter optimization. Random search differs from grid search in that you no longer provide a discrete set of values to explore for each hyperparameter; instead, you provide a statistical distribution for each hyperparameter from which values are randomly sampled and set the total number of combinations you want to try. Bayesian techniques differ from random or grid search in that they use past evaluation results to choose the next values to evaluate.
There are also gradient-based techniques, evolutionary optimization techniques, and other algorithmic hyperparameter tuning techniques.