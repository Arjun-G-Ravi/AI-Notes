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

