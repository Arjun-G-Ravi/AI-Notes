# How to train a NN effectively

- Get training data
  - Data exploration and analysis
  - Finding what data is relevand and what is not

- Preprocess training data
  - Normalization and Standardisation
  - Batching
  - Splitting to train/val/test sets
  - Manage missing data
  - Data augmentation
  - Feature engineering(modify existing features and create new ones)

- Designing ML model
  - Basic ML model design
    - Design model architecture
    - Hyperparameter tuning
    - Proper loss function
    - Proper optimisation function
    - Model validation
      - K-fold cross-validation
      - stratified sampling
    - Model evaluation
      - Proper metric selection

  - Optimising the training process
    - Parameter initialization
    - Layer/ Batch normalisation
    - Residual connections
    - Regularisation
      - Dropout
      - Weight decay
    - Early stopping
    - Learning rate decay/ scheduling
    - Gradient clipping
    - Warm up phase

  - Hardware optimisations
    - Parallel training
    - Mixed Precision Training