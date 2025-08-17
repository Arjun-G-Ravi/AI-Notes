# Hyperparameter Tuning

Hyperparameters are variables that are not optimized by the learning algorithm, but by the ML programmer. The data analyst has to “tune” hyperparameters by experimentally finding the best combination of values, one per hyperparameter.

One method is grid search, but trying all combinations of hyperparameters, especially if there are more than a couple of them, could be time-consuming.

There are more efficient techniques, such as random search and Bayesian hyperparameter optimization. Random search differs from grid search in that you no longer provide a discrete set of values to explore for each hyperparameter; instead, you provide a statistical distribution for each hyperparameter from which values are randomly sampled and set the total number of combinations you want to try. Bayesian techniques differ from random or grid search in that they use past evaluation results to choose the next values to evaluate.

There are also gradient-based techniques, evolutionary optimization techniques, and other algorithmic hyperparameter tuning techniques.

In practical applications, hyperparameter tuning is often done using cross-validation to ensure that the model generalizes well to unseen data. We use tools like optuna or hyperopt to automate the hyperparameter tuning process, which can significantly speed up the search for optimal hyperparameters.