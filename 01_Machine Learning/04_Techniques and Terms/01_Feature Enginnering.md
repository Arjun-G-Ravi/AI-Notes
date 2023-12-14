# Feature Engineering
A feature vector is an ordered list of numerical properties of an observed phenomenon. It represents input features to a machine learning model that makes a prediction. The problem of transforming raw data into a dataset, which can be used by a ML model is called feature engineering.

## 1. One-Hot Encoding
Some learning algorithms only work with numerical feature vectors. So we reperesent each class in  a feature as a separate feature and assign that feature to have 0 or 1.

For eg: Instead of

``` colors = [“red”, “blue”, “green”] ```

we design three features as

``` red = [1, 0, 0] blue = [0, 1, 0] green = [0, 0, 1]```

You should not transform red into 1, yellow into 2, and green into 3 to avoid increasing the dimensionality because that would imply that there’s an order among the values in this category and this specific order is important for the decision making. If the order of a feature’s values is not important, using ordered numbers as values is likely to confuse the learning algorithm, because the algorithm will try to find a regularity where there’s no one, which may potentially lead to overfitting.

## 2. Binning
An opposite situation, occurring less frequently in practice, is when you have a numerical feature but you want to convert it into a categorical one. Binning (also called bucketing) is the process of converting a continuous feature into multiple binary features called bins or buckets, typically based on value range.

For eg, A dataset with individuals' income datacan be categorized by their income levels into three bins: "Low Income," "Medium Income," and "High Income."

In some cases, a carefully designed binning can help the learning algorithm to learn using fewer examples. It happens because we give a “hint” to the learning algorithm that if the value of a feature falls within a specific range, the exact value of the feature doesn’t matter.

## 3. Feature Scaling
This involves scaling the datapoints so that the ML algorithm will have a good time with learning them. There are two feature scaling methods: Normalisation and Standardisation.

#### Normalisation
Normalization is the process of converting an actual range of values which a numerical feature can take, into a standard range of values, typically in the interval [−1, 1] or [0, 1]. Normalizing the data is not a strict requirement. However, in practice, it can lead to an increased speed of learning. Additionally, it’s useful to ensure that our inputs are roughly in the same relatively small range to avoid problems which computers have when working with very small or very big numbers (known as numerical overflow).

#### Standardization
Standardization (or z-score normalization) is the procedure during which the feature values are rescaled so that they have the properties of a standard normal distribution with µ = 0 and σ = 1, where µ is the mean and σ is the standard deviation from the mean.

## 4. Dealing with Missing Features
The typical approaches of dealing with missing values for a feature include:
- removing the examples with missing features from the dataset
- using a learning algorithm that can deal with missing feature values 
- using a data imputation technique.

#### Data Imputation Techniques
- One data imputation technique consists in replacing the missing value of a feature by an average value of this feature in the dataset.

- Another technique is to replace the missing value with a value outside the normal range of values.For example, if the normal range is [0, 1], then you can set the missing value to 2 or −1.
  
- Alternatively, you can replace the missing value by a value in the middle of the range. For example, if the range for a feature is [−1, 1], you can set the missing value to be equal to 0.Here, the idea is that the value in the middle of the range will not significantly affect the prediction.
  
- A more advanced technique is to use the missing value as the target variable for a regression problem. You can use all remaining features to form a feature vector, where j is the feature with a missing value. Then you build a regression model to predict ŷ from x̂. Of course, to build training examples (x̂, ŷ), you only use those examples from the original dataset, in which the value of feature j is present.
  
- Finally, if you have a significantly large dataset and just a few features with missing values, you can increase the dimensionality of your feature vectors by adding a binary indicator feature for each feature with missing values.


