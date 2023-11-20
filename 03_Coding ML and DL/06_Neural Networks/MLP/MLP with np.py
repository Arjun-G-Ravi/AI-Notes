# incomplete

import numpy as np

class MLP:
    def __init__(self,lr=0.01, num_epochs=100, layers=[3,2,1]):
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
            w = np.random.rand(shape_for_weight, i)  # -.5
            self.weight.append(w)
            bias = np.zeros([1,i])
            self.bias.append(bias)
            shape_for_weight = i    


        # forward pass
        X_out, layer_cache = self.predict(X)

        # define loss
        modified_log = lambda inp:0 if inp==1 else -1  # defined only for domain {0,1} ;)
        loss = ([-y_i*modified_log(f_x_i)-(1-y_i)*modified_log(1-f_x_i) for (y_i, f_x_i) in zip(y,X_out)])
        total_loss = (1/m)*np.sum(loss)

        # backpropogation
        print(total_loss)
        for i in layer_cache:
            for j in i:
                print(j.shape)

        for z_i,w_i,b_i in layer_cache[::-1]:
            print(z_i)

        return 

    def predict(self, X):
        X_traversing = X
        layer_cache = []
        for i,v in enumerate(self.layers[:-1]): # all except the last layer
            weight = self.weight[i]
            bias = self.bias[i]
            X_traversing = X_traversing @ weight + bias
            layer_cache.append((X_traversing, weight, bias))
            X_traversing = self.relu(X_traversing)

        # last layer
        weight = self.weight[-1]
        bias = self.bias[-1]
        X_traversing = X_traversing @ weight + bias
        layer_cache.append((X_traversing, weight, bias))
        X_traversing = self.sigmoid(X_traversing)

        X_out = X_traversing
        X_out = [1 if x>0.5 else 0 for x in X_traversing]
        return X_out, layer_cache

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
    X, y = datasets.make_classification(n_samples=100, n_features=2, n_classes=2, n_redundant=0, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
    obj = MLP()
    obj.fit(X_train, y_train)
    # obj.predict(X_train)
