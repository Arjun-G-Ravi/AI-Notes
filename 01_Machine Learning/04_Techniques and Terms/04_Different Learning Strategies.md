# 1.Multiclass Classification
For multiclass classification problems, we extend the logistic regression to softmax regression algorithm. This is done by replacing sigmoid function in logistic regression with softmax function. 

The loss function in softmax regression is typically the cross-entropy loss (also known as log-loss). Given a set of training examples, the cross-entropy loss measures the dissimilarity between the predicted probabilities and the true class labels. 

					- log a1, if y == 1
					- log a2, if y == 2
			L  =  			:
						:
					- log an, if y == n

Where``` aj = ezj / ΣNk=1 = P(y = j | x)```  , where N is the number of classes

# 2. One class classification
One-class classification, also known as unary classification or class modeling, tries to identify objects of a specific class among all objects, by learning from a training set containing only the objects of that class. The most widely used in practice are one-class Gaussian, one-class k-means, one-class kNN, and one-class SVM.

# 3. Multi-Label Classification
In some situations, more than one label is appropriate to describe an example from the dataset. In this case, we talk about the multi-label classification. The only difference with the usual multiclass problem is that now we have a new hyperparameter: threshold. If the prediction score for some label is above the threshold, this label is predicted for the input feature vector. In this scenario, multiple labels can be predicted for one feature vector.

# 4. Active Learning
The idea is to start training a supervised model with relatively few labeled examples, and a large number of unlabeled ones, and then label only those examples that contribute the most to the model quality. It is usually applied when obtaining labeled examples is costly.

Data density and uncertainty based model: For each unlabeled example x, the following importance score is computed: density(x) * uncertainty(x). Density for the example x can be obtained by taking the average of the distance from x to each of its k nearest neighbors. Once we know the importance score of each unlabeled example, we pick the one with the highest importance score and ask the expert to annotate it.

SVM based model: The support vector-based active learning strategy consists in building an SVM model using the labeled data. We then ask our expert to annotate the unlabeled example that lies the closest to the hyperplane that separates the two classes.


# 5. Semi-Supervised Learning
In semi-supervised learning (SSL) we also have labeled a small fraction of the dataset; most of the remaining examples are unlabeled. Our goal is to leverage a large number of unlabeled examples to improve the model performance without asking for additional labeled examples.
### Self-learning
One frequently cited SSL method is called self-learning. In self-learning, we use a learning algorithm to build the initial model using the labeled examples. Then we apply the model to all unlabeled examples and label them using the model. If the confidence score of prediction for some unlabeled example x is higher than some threshold (chosen experimentally), then we add this labeled example to our training set, retrain the model and continue like this until a stopping criterion is satisfied. We could stop, for example, if the accuracy of the model has not been improved during the last m iterations.

# 6. One shot learning
One-shot learning is a machine learning paradigm that focuses on training models to recognize and classify objects or patterns based on just a single or very few examples of each class. One way to effectively solve the problem is to train a siamese neural network (SNN). To train an SNN, we use the triplet loss function. 

# 7. Zero-shot learning
Zero-shot learning (ZSL) is a machine learning paradigm where a model is trained to recognize and classify objects or concepts it has never seen during the training phase. For eg, it could be to predict  a the class of the object, if that class name and object was never in the training data.

# 8. Transfer Learning
In transfer learning, you pick an existing model trained on some dataset, and you adapt this model to predict examples from another dataset, different from the one the model was built on.

Neural networks excel in transfer learning by enabling a process where you extract the benefits of pre-trained models. You start by discarding the final one or more layers of the original model, typically responsible for classification or regression. Then, you customize the model by introducing new layers tailored to your specific problem. To retain the valuable knowledge gained from the initial training, you "freeze" the parameters of the remaining layers from the original model.




