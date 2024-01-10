# Dimensionality Reduction
Three widely used techniques of dimensionality reduction are principal component analysis (PCA), uniform manifold approximation and projection (UMAP), and autoencoders.

<!-- Why did i write this thing here? -->
## Autoencoders
You can use the low-dimensional output of the bottleneck layer of the autoencoder as the vector of reduced dimensionality that represents the high-dimensional input feature vector.

## Principal Component Analysis
-  PCA Defines a New Coordinate System - it identifies a new set of axes, called principal components, to represent the data. These axes are chosen to maximize the variance of the data along each axis.
-  First Principal Component: The first principal component represents the direction in the data space along which the data varies the most. It accounts for the highest variance in the data.
-  Orthogonal Axes: Subsequent principal components are orthogonal (perpendicular) to the previous ones. This ensures that each component captures a unique and uncorrelated source of variance in the data.
-  Sequential Capture of Variance: If the data is three-dimensional, PCA will determine the first principal component along the axis of highest variance, the second principal component along the axis of second-highest variance, and so on for higher-dimensional data.
-  Dimensionality Reduction: After identifying the principal components, you can choose to retain a subset of them to reduce the dimensionality of the data. This can be particularly useful when dealing with high-dimensional data while preserving most of the data's information.


## UMAP
Another dime redn technique