# incomplete

import numpy as np

class MLP:
    def __init__(self,lr=0.01, num_epochs=100, layers=[25, 364, 895, 1040, 568, 32, 48, 1]):
        self.lr = lr
        self.num_epochs = num_epochs
        self.layers = layers
        self.num_layers = len(layers)
        self.weight = [] # weight.shape = (num_layers X num_neurons_per_layer X num_feature in a neuron )
        self.bias = [] # bias.shape = (num_layers X num_neurons_per_layer X 1 in a neuron )
        

    def fit(self, X, y):
        m, n = X.shape # num_data X num_features

        # defining shape of weights and initializing them with random nos btw 0 and 1
        shape_for_weight = n
        for i in self.layers:
            w = np.random.rand(shape_for_weight, i)
            self.weight.append(w)
            bias = np.random.rand(i)
            self.bias.append(bias)
            shape_for_weight = i    


    # BACK PROPOGATION  
        # forward pass
        X_out = self.predict(X)

        print(X_out)
        return 

    def predict(self, X):
        X_traversing = X
        for i,v in enumerate(self.layers[:-1]): # all except the last layer
            weight = self.weight[i]
            bias = self.bias[i]
            X_traversing = X_traversing @ weight + bias
            X_traversing = self.relu(X_traversing)

        # last layer
        weight = self.weight[-1]
        bias = self.bias[-1]
        X_traversing = X_traversing @ weight + bias
        X_traversing = self.sigmoid(X_traversing)



        X_out = X_traversing
        X_out = [1 if x>0.5 else 0 for x in X_traversing]
        return X_out

    def relu(self,X):
        return np.maximum(0, X)

    def sigmoid(self, x):
        out = 1/(1+np.exp(-x))
    
        # print(out.shape)
        return out

# test
if __name__ == '__main__':
    from sklearn.model_selection import train_test_split
    from sklearn import datasets
    X, y = datasets.make_blobs(n_samples=100, n_features=2, cluster_std=1.05, random_state=2)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
    print('X.shape=',X_train.shape)

    obj = MLP()
    obj.fit(X_train, y_train)
    # obj.predict(X_train)
