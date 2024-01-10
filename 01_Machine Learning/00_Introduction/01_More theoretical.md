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


### TO UPDATE ...