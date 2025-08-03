# Tips for Kaggle Competitions
- Add topic specific knowlege to your model.
- Use public features and models that are already available in discussion forums.
- Have a base stucture which will let you quickly add new features and models and ensemble them with your existing models.
- Validation Strategy
- (Most of the times) Only Boosted Trees and Neural Networks wins in Kaggle competitions.
- You need an ensemble of models to win.
- You need to (eventually) develop a validation environment that mimics the competition environment. This allows you to test your models and features as many times as you want, and will prevent your model from overfitting to the submission environment.
- 
- csv files can lose precision, so use pickle files to save your models.
- AutoML tools can be used to quickly get a baseline model, but they might not always yield the best results.

# Important Skills
- Data Preprocessing and Visualization (to identify patterns and anomalies for feature engineering)
- Feature Engineering (more important than the model)
- Model Ensembling - stacking, voting
- Hyperparameter Tuning - optuna
- Model Validation - custom validation strategies, cross-validation(k-fold, stratified, etc.)