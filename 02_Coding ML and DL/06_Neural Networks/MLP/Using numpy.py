# incomplete

import numpy as np

class MLP:
    def __init__(self,lr=0.01, num_epochs=100, layers=[1, 3, 1]):
        self.lr = lr
        self.num_epochs = num_epochs
        self.layers = layers
        self.num_layers = len(layers)
        self.weight = [] # weight.shape = (num_layers X num_neurons_per_layer X num_feature in a neuron )
        self.bias = [] # bias.shape = (num_layers X num_neurons_per_layer X 1 in a neuron )
        

    def fit(self, X, y):
        m, n = X.shape # num_data X num_features
        for i in self.layers:
            bias_per_layer = []
            wt_per_layer = []
            for j in range(i): # me completely forgot the existence of np.zeros() :0
                wt_of_that_neuron = [0 for k in range(n)] # make it random
                bias_of_that_neuron = [0] # make it random
                wt_per_layer.append(wt_of_that_neuron)
                bias_per_layer.append(bias_of_that_neuron)
            self.weight.append(wt_per_layer)
            self.bias.append(bias_per_layer)
        # print(self.weight)
        return 

    def predict(self, X):
        to_next_layer = X
    

        return
    
    def sigmoid(self, x):
        return 1/(1+np.exp(-x))
        
    def sigmoid_derivative(self, x): # Derivative of the sigmoid activation function
        return x*(1-x)


# test
if __name__ == '__main__':
    from sklearn.model_selection import train_test_split
    from sklearn import datasets
    X, y = datasets.make_blobs(n_samples=100, n_features=2, cluster_std=1.05, random_state=2)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

    obj = MLP()
    obj.fit(X_train, y_train)
    obj.predict(X_train)
