# Decision Tree Algorithm
The Decision Tree Algorithm is a supervised ML algorithm that leverages tree data structure. Every input is passed into a tree structure. In each branching node of the tree, a specific feature of the feature vector is examined. If the value of the feature is below a specific threshold, then the left branch is followed; otherwise, the right branch is followed. As the leaf node is reached, the decision is made about the class to which the example belongs.

![Alt text](image-3.png)

Trees can be **univariate** [each decision node makes decision using only one feature] (like ID3), or **multivariate**.


The picture shows how the data is split into sections, for the tree to split.
![Alt text](<Screenshot from 2023-12-14 12-56-48.png>)

### Notes:
- A decision tree can be converted to a set of IF-THEN rules that are easily understandable. For this reason, decision trees are very popular and sometimes preferred over more accurate but less interpretable
methods.

- Decision Trees are non parametric in nature. Non-parametric models make fewer assumptions about the underlying data distribution and aim to capture patterns directly from the data. These models can adapt to more complex relationships without assuming a specific functional form. They often require storing the entire training dataset, making them memory-intensive. ```They don’t create a compressed model that can be used to perform inference(like linear regression finding w* and b*).```

- As each feature is processed separately, and the possible splits of the data don’t depend on scaling. No preprocessing like normalization or standardization of features is needed for decision tree algorithms.

- They are super prone to overfitting, so some regularisation means is required.
- They are also very sensitive to data. Small change in data can result in a completely different tree.
  
# Types of Decision Trees
Decision Trees are of two types:
 1. Classification trees
 2. Regression trees

### Classification Trees
In the case of a decision tree for classiﬁcation, namely, a classiﬁcationtree, the goodness of a split is quantiﬁed by an impurity measure.A split is pure if after the split, for all branches, all the instances choosing a branch belong to the same class. There are multiple functions which can be used to quatify the impurity.

##### 1. Entropy
Entropy is a measure of impurity or disorder in a set of data. It is commonly used in decision tree algorithms, such as ID3 (Iterative Dichotomiser 3), C4.5, and CART (Classification and Regression Trees), to determine the best feature to split the data at each node.

The goal is to find the feature and the corresponding split point that minimizes entropy, creating more homogeneous subsets in the tree. This approach helps the decision tree algorithm to make decisions that lead to more accurate predictions.

It is defined for a feature, and is equal to
```
H(p) = ∑(for each class in the feature) −p*log2(p) − (1−p)*log2 (1−p)
```
where p is the probability where that class yields "True" or "yes".

##### 2. Gini Index
Similar to entropy, but defined as ```H(p) = 2p(1 − p)```

### Regression Trees
They are decision trees used to perform regression. In regression, the goodness of a split is measured by the mean square error from the estimated value. In a node, we use the mean (median if there is too much noise) of the required outputs of instances reaching the node. 

# Pruning
Pruning in decision trees is a technique used to reduce the complexity of a decision tree model by removing branches (subtrees) that do not provide significant predictive power and may lead to overfitting. 

#### Prepruning
Frequently, a node is not split further if the number of training instances reaching a node is smaller than a certain percentage of the training set for example, 5 percent—regardless of the impurity or error. The idea is that any decision based on too few instances causes variance and thus generalization error. Stopping tree construction early on before it is full is called prepruning the tree.

#### Postpruning
In postpruning, we grow the tree full until all leaves are pure and wehave no training error. We then ﬁnd subtrees that cause overﬁtting and we prune them.


## Random Forest
A random forest is essentially a collection of decision trees, where each tree is slightly different from the others. The idea behind random forests is that each tree might do a relatively good job of predicting, but will likely overfit on part of the data. If we build many trees, all of which work well and overfit in different ways, we can reduce the amount of overfitting by averaging their results. Also, instead of looking for the best test for each node in each node,  the algorithm randomly selects a subset of the features, and it looks for the best possible test involving one of these features.

The randomness in building the random forest forces the algorithm to consider many possible explanations, the result being that the random forest captures a much broader picture of the data than a single tree.

## Gradient boosted regression trees
The gradient boosted regression tree is another ensemble method that combines multiple decision trees to create a more powerful model. Despite the “regression” in the name, these models can be used for regression and classification. In contrast to the random forest approach, gradient boosting works by building trees in a serial manner, where each tree tries to correct the mistakes of the previous one. By default, there is no randomization in gradient boosted regression trees; instead, strong pre-pruning is used. Gradient boosted trees often use very shallow trees, of depth one to five, which makes the model smaller in terms of memory and makes predictions faster.
Eg: XGBoost