# Design matrix
- ML models are trained with lots of data
- Generally, data is stored in design matrix - with features as columns and data examples as rows, as NxD matrix
  - if N>>D: tall and skinny shape -> big data
  - if N<<D: short and fat shape -> wide data
- Some data(such as text and image) are not stored in design matrix. But before they are used in a ML model, they are usually converted to fixed size form(design matrix form).

## Empirical risk minimization
The goal of our model is to optimise its parameters such that the risk(a loss function) is minimised.

# Uncertainty
A stochastic process is one that is governed by chance or probability, rather than being deterministic or predictable. Many machine learning algorithms, such as stochastic gradient descent, involve stochastic processes to optimize model parameters.

In many cases, we will not be able to perfectly predict the exact output given the input, due to lack of knowledge of the input-output mapping (this is called epistemic uncertainty or `model uncertainty`), and/or due to intrinsic (irreducible) stochasticity in the mapping (this is called aleatoric uncertainty or data uncertainty).

Representing uncertainty in our prediction can be important for various applications. So for many classification models, instead of returning the highest value output, we pass them through a softmax layer(which gives probability for each class). The inputs to softmax are called logits.

# Maximum Likelihood Estimation
MLE is a statistical framework that assumes a specific probability distribution for the data, and the goal is to find the parameters that maximize the likelihood of observing the data. This framework is typically used in parametric statistics, where the underlying distribution is assumed to be known (e.g., normal, binomial, Poisson). Many ML model fall under this category. Some dont: 
- Regression: They are considered as MLE
- Neural Networks: Use methods related to MLE for training but do not assume a specific data distribution.
- Decision Trees: Do not assume a specific probability distribution and are not typically considered MLE models. Instead, they use a non-parametric approach based on data splitting criteria.

# No free lunch theorem
There is no single best model that works optimally for all kinds of problems — this is sometimes called the no free lunch theorem. The reason is that a set of assumptions (also called inductive bias) that works well in one domain may work poorly in another.

## Exploratory data analysis
Before tackling a problem with ML, it is usually a good idea to perform exploratory data analysis, to see if there are any obvious patterns (which might give hints on what method to choose), or any obvious problems with the data (e.g., label noise or outliers).

It can include:
 - making a pair plot for each feature
 - dimensionality reduction