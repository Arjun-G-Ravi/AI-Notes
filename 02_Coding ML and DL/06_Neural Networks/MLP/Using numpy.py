import numpy as np

class MLP:
    def __init__(self,lr=0.01, num_epochs=100, neurons_per_layer=[10,10]):
        self.lr = lr
        self.num_epochs = num_epochs
        self.neurons_per_layer = neurons_per_layer
        self.num_layers = len(neurons_per_layer)
        self.weight = None
        self.bias = None
        
    def fit():
        pass
    def predict():
        pass
    
    def activation_function(self, x):
        return max(x, 0)
    
    def sigmoid(self, x):
        return 1/(1+np.exp(-x))
    