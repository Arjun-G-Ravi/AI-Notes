# Vectorisation and Broadcasting
Vectorization and broadcasting are techniques used in Python, particularly with libraries like NumPy and Pytorch, to boost the speed and efficiency of numerical operations on arrays or matrices. 

## Vectorization
Vectorization is the process of rewriting a loop-based, scalar computation to work on entire arrays or vectors at once. Instead of performing operations element-wise, you apply operations directly to the entire array. It significantly speeds up numerical computations because it takes advantage of low-level optimizations provided by libraries like NumPy.

Eg: Using np.dot(m1,m2) instead of multiplying over a loop


## Broadcasting
Broadcasting is a technique used in NumPy (and similar libraries) to perform operations on arrays with different shapes, making them compatible without creating unnecessary copies of data. It allows you to perform element-wise operations on arrays of different shapes, which can simplify code and reduce memory usage. It's particularly useful when working with arrays of differing dimensions.

Eg: arr + 3, adds 3 to every element in the array by broadcasting.