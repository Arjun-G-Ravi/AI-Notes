## Object Classification
Classifing the object in an image as one among a lot of classes.

## Object Localisation
Image localization, often referred to as object localization, is a computer vision task that involves identifying and precisely locating one or more objects within an image.
The goal is to determine the coordinates or bounding box that delineates the region of interest where the object(s) are located.

## Landmark Detection
Detecting various important landmark in an image. Eg: Posture of a man

## Object Detection
The act of detecting an object and localising it. 

## Sliding Window Detection
One object detection method, where we slide an incresingly bigger window over an image with a very small stride, in the hope to fit the box on the image. But this is very inefficient.
![Alt text](<Screenshot from 2023-10-18 20-15-23.png>)

We can implement convolution over this to make this more efficient.

#### Learn yolo algorithm, u-net algo

## One shot learning
One-shot learning is a machine learning and computer vision technique designed for tasks where you have very limited data for each category or class. 

It can be implemented by defining some function that maps the difference between the trained data, against the image to classify. If this function stays in a threshold, we can say that the image is classified to the corresponding label. 

This function can be implemented via methods like siamese network, which makes encodings of the image and compares the encodings.

## Triplet Loss
![Alt text](<Screenshot from 2023-10-18 21-29-57.png>)