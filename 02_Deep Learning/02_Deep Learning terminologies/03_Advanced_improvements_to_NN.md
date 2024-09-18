# Exponentially weighted average
Exponentially weighted average is a statistical technique that give `more weight to recent data points, while diminishing the influence of older data points`.

This is a technique that can be used in DL optimisation to update paramters based on influence from earlier parameters. -> `used in momentum`

y(t) = beta*y(t-1) + (1-beta)*f(x)

Bias correction can be implemented in this to make this more accurate.

# Gradient Descent with momentum
The basic idea is to `compute an exponentially weighted average of your gradients, and then use that gradient to update your weights`.

- This is helpful if the gradient has to go slow in one direction and fast in the other, as it creates a kind of "momentum" from the previous weight update. 
- We can use a larger lr, and converge faster. 
- May help avoid local minimas
- Makes the choice of lr obselete.
- Loss may go up and down, during training

For momentum, the weight gets updated as:

    w(t) -> w(t-1) - dJ_dw(t)*lr + alpha * w(t-1)

![Alt text](<Screenshot from 2023-10-12 21-11-00.png>)

# RMSprop
Just like Grad desc with moementum, with a small algorithmic change.
RMSprop, which stands for Root Mean Square Propagation, is an optimization algorithm commonly used in training machine learning models, particularly deep neural networks.
Traditional gradient descent methods use a fixed learning rate for all parameters, which may lead to slow convergence or divergence in some cases. `RMSprop adjusts the learning rates based on the historical gradient information for each parameter`.

It helps to converge faster and reach better solutions by scaling the learning rates based on the historical gradient information.

![Alt text](<Screenshot from 2023-10-12 21-24-45.png>)

# Adam Optimisation algorithm
The Adam (Adaptive Moment Estimation) optimization algorithm is basically taking `momentum and RMSprop`, and putting them together. Generally, bias correction and mini-batching is also done in Adam. It is way superrior to gradient descent for optimisation purposes.

![Alt text](<Screenshot from 2023-10-13 06-35-25.png>)

# Learning Rate Decay
One of the things that might help speed up your learning algorithm is to `slowly reduce your learning rate over time`. This is called learning rate decay, and can be implemented as:

![Alt text](<Screenshot from 2023-10-13 06-39-52.png>)

This works, because we might want a large lr at the start, and smaller ones as we get to the end of the optimisation process.

![Alt text](<Screenshot from 2023-10-13 06-41-27.png>)

# Data Augmentation
Data augmentation is a technique used in machine learning, particularly in computer vision and natural language processing, to artificially increase the size of a training dataset by applying various transformations to the existing data.
It includes:
 - Rotation, Mirroring, Random cropping(5-crop, etc.), etc.
 - Color shifting (shift RGB values by a small value)