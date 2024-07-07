# Design matrix
- ML models are trained with lots of data
- Generally, data is stored in design matrix - with features as columns and data examples as rows, as NxD matrix
  - if N>>D: tall and skinny shape -> big data
  - if N<<D: short and fat shape -> wide data
- Some data(such as text and image) are not stored in design matrix. But before they are used in a ML model, they are usually converted to fixed size form(design matrix form).

## Empirical risk minimization
The goal of our model is to optimise its parameters such that the risk(a loss function) is minimised.