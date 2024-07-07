# Types of ML Algorithms
There are two types of ML algorithms: Supervised and Unsupervised.

# 1. Supervised Algorithms
Supervised algorithms are a type of machine learning algorithm that learn from labeled training data to make predictions or decisions. They are of two types - Regression and Classification.

## a. Regression
Regression algorithms are used when the target variable we want to predict is continuous. A commmon loss function is sqared error loss.
Eg: Linear Regression, Regression Trees, etc.

## b. Classification
Classification algorithms are used when the target variable we want to predict is discrete or categorical. A common loss fn used is negative log likelihood loss.
Eg: KNn, Logistic Regression, SVM, etc.

### Generative and Discriminative Classifiers
Classification algorithms are of two types - Generative and Discriminative. 

`Generative classifiers focus on modeling the underlying data distributions.` One advantage of generative classifiers is that they can provide insights into the underlying distributions of the data, which can be useful for exploratory analysis and hypothesis testing.
Eg: Naive bayes, Gaussian Discriminant Analysis, Hidden Markov Models, etc.

`Discriminative classifiers focus on finding decision boundaries that separate the classes.` They tend to perform better than generative classifiers in terms of prediction accuracy, especially when dealing with high-dimensional data or complex relationships between variables.
Eg: Logistic regression, SVM, trees, NN, etc