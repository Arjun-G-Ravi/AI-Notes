# Ensemble learning
Ensemble learning is a learning paradigm that, instead of trying to learn one super-accurate model, focuses on training a large number of low-accuracy models and then combining the predictions given by those weak models to obtain a high-accuracy meta-model.

Low-accuracy models are usually learned by weak learners, that is, learning algorithms that cannot learn complex models, and thus are typically fast at the training and at the prediction time. The most frequently used weak learner is a decision tree learning algorithm in which we often stop splitting the training set after just a few iterations. The obtained trees are shallow and not particularly accurate, but the idea behind ensemble learning is that if the trees are not identical and each tree is at least slightly better than random guessing, then we can obtain high accuracy by combining a large number of such trees. To obtain the prediction for input x, the predictions of each weak model are combined using some sort of weighted voting. Two principal ensemble learning methods are boosting and bagging.

### Boosting and Bagging
Boosting consists of using the original training data and iteratively creating multiple models by using a weak learner. Each new model would be different from the previous ones in the sense that the weak learner, by building each new model tries to “fix” the errors which previous models make. The final ensemble model is a certain combination of those multiple weak models built iteratively.

Bagging consists of creating many “copies” of the training data (each copy is slightly different from another) and then apply the weak learner to each copy to obtain multiple weak models and then combine them. A widely used and effective machine learning algorithm based on the idea of bagging is random forest.

### Random Forest
Random Forest is a specific implementation of bagging that is tailored for decision trees and incorporates feature randomness to further enhance its performance and robustness. In a Random Forest, multiple decision trees are trained on different subsets of the data using sampling with replacement and with random feature subsets. The predictions from these individual trees are then combined to make a final prediction, typically through a majority vote for classification tasks or averaging for regression tasks Also, instead of looking for the best test for each node in each node,  the algorithm randomly selects a subset of the features, and it looks for the best possible test involving one of these features..

Random forest is one of the most widely used ensemble learning algorithms. The reason is that by using multiple samples of the original dataset, we reduce the variance of the final model, lowering overfitting. 

### Gradient Boosting
Gradient boosting is a modified boosting algorithm that implements a gradient descent (in a non traditional way) to calculate the error caused by the ensemble trees. This error is used to update the trees, training the model and reducing the error. However, instead of getting the gradient directly, we use its proxy in the form of residuals: they show us how the model has to be adjusted so that the error (the residual) is reduced. It reduces underfitting, but can lead to overfitting. So careful selection of hyperparameters is adviced.

In contrast to the random forest approach, gradient boosting works by building trees in a serial manner, where each tree tries to correct the mistakes of the previous one. By default, there is no randomization in gradient boosted regression trees; instead, strong pre-pruning is used. Gradient boosted trees often use very shallow trees, of depth one to five, which makes the model smaller in terms of memory and makes predictions faster.
Eg: XGBoost

Gradient boosting is one of the most powerful machine learning algorithms—not just because it creates very accurate models, but also because it is capable of handling huge datasets with millions of examples and features. It usually outperforms random forest in accuracy but, because of its sequential nature, can be significantly slower in training.

# Combining Models
A modification to be done to ensemble method is to use various models (of different architectures) to create an ensemble. Three typical ways to combine models are 
1) averaging
2) majority voting
3) stacking