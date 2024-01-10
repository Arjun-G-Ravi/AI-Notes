### Hypothesis Space:
The hypothesis space refers to the set of all possible hypotheses or candidate models that a machine learning algorithm can create to make predictions or classifications. 

The purpose of ML is to select a hypothesis(model) from the hypothesis space that will approximate input to output.

Eg: In linear regression, the hypothesis space consists of all possible linear functions that can be used to map input features to output labels.

### Version Space
The version space is the subset of the hypothesis space that is still considered plausible or feasible given the available evidence. All the hypothesis present in the version space will be able to correctly classify input to output from the dataset.


### VC Dimension
The Vapnik-Chervonenkis (VC) dimension is a concept in statistical learning theory and machine learning that measures the capacity or expressive power of a hypothesis class. 

- For a binary classification for m datapoints in n dimension, we have H which is a set of all hypothesis classes. 
- If a hypothesis h∈H can correctly classify all m datapoints in n dimensions, we say that H shatters the dataset. 
- The VC dimension of the hypothesis class H is the maximum number of datapoints that H can shatter. 

# PAC Learning
PAC (Probably Approximately Correct) learning is a theoretical framework in machine learning that focuses on creating algorithms to learn concepts from data. The goal is to design algorithms that, with high probability, can accurately generalize from a limited set of examples to new, unseen data. The framework considers how well the learning algorithm can approximate the true underlying concept and how many examples are needed for reliable learning. It aims to provide probabilistic guarantees for the correctness of learned models.

PAC learning is a specific theoretical framework within the broader field of machine learning. While PAC learning principles are foundational to understanding the generalization and reliability of learning algorithms, not all of machine learning is explicitly framed within the PAC model.

In practical terms, many machine learning algorithms and techniques used today draw inspiration from the principles of PAC learning. PAC learning focuses on the probabilistic correctness and efficiency of learning algorithms, addressing questions about how well they generalize to new, unseen data.

So, you could say that PAC learning is a subset or specific perspective within the field of machine learning, providing theoretical foundations for understanding the learning process and the generalization performance of algorithms.

# Inductive Bias
The set of assumptions we make to have learning possible is called the inductive bias of the learning algorithm. Learning is a very huge problem, and these inductive biases are what makes it possible.

# Maximum Likelihood Estimation (MLE)

MLE stands for Maximum Likelihood Estimation. It is `a method used in statistics to estimate the parameters of a statistical model`. The fundamental idea behind MLE is to find the values of the model parameters that maximize the likelihood function, which measures how well the model explains the observed data.

### Likelihood Function:
The likelihood function represents the probability of observing the given data under a particular set of parameter values. In other words, it measures how likely the observed data is for different parameter values.

### Log-Likelihood Function:
Because likelihood values can become very small, it is common to work with the log-likelihood function instead. This doesn't change the position of the maximum likelihood estimates but simplifies computations.

### MLE
MLE involves finding the values of the model parameters that maximize the likelihood (or log-likelihood) function.

# Correlation Matrix
A correlation matrix is a table showing correlation coefficients between variables. Each cell in the table represents the correlation between two variables. Correlation measures the strength and direction of a **linear** relationship between two variables.

- Corr=1: Perfect positive correlation (as one variable increases, the other also increases proportionally).
- Corr=−1: Perfect negative correlation (as one variable increases, the other decreases proportionally).
- Corr=0: No linear correlation.

`Just because Corr of two variables is zero, doesn't mean that they are unrelated. They can have a NON-LINEAR relationship.`

It can be used in pandas using df.corr().

