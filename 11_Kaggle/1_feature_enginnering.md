# Feature Engineering
Feature engineering is the process of transforming raw data into features that better represent the underlying problem to the predictive models, resulting in improved model accuracy on unseen data.

# Feature Extraction
- Feature extraction is the process of extracting useful information from raw data. 
- It typically reduces the dimensionality of the data while retaining important information using techniques like Principal Component Analysis (PCA), Singular Value Decomposition (SVD), or autoencoders.

# Feature Selection
- Feature selection is the process of selecting a subset of relevant features for use in model construction. 
- Feature selection algorithms may use a scoring method to rank and choose features, such as correlation or other feature importance methods.
- More advanced methods may search subsets of features by trial and error, creating and evaluating models automatically in pursuit of the objectively most predictive sub-group of features.
- Regularization methods like L1 (Lasso) and L2 (Ridge) can automatically select features by penalizing less important ones.

## How to do Feature Engineering
1. Apply mathematical operations on features.
2. Add different features together after doing Step 1
3. Split features into multiple features.
4. Use domain knowledge to create new features.


# Feature Learning
Feature learning or representation learning is a set of techniques that allow a system to automatically discover the representations needed for feature detection or classification from raw data. This replaces manual feature engineering and allows a machine to both learn the features and use them to perform a specific task. 