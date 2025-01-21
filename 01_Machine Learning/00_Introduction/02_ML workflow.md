# Basic ML workflow
    1) Data collection
    2) Exploratory data analysis
    3) Data preprocessing, splitting, analysis and feature engineering
    4) Model selection 
    		a) Regression - Linear regression, Polynomial regression, Regression trees  
    		b) Classfication - Logistic regression, Decision trees, SVM, K-nearest neighbours
   			c) Dimensionality reduction - PCA
    		d) Clustering - K-means
    		e) General(pretty much everything) - NNs 
    5) Model training
    	• Perform forward prop and compare it with the target to obtain an error measurement
    	• Use this error measurement to define loss function
    	• Extend loss function to entire dataset to get the cost function – the objective function
    	• Choose any optimisation algorithm (like  Gradient Descent) for optimising the objective function, inorder to reduce the loss/cost. 
    	• Repeat for any number of epoch you want
    6) Model evaluation - errors, accuracy, precision, recall, F1-score, etc.
    7) Model deployment/ monitoring/ maintainance