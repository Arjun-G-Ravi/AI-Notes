import numpy as np

# Define the activation function (e.g., sigmoid)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Hyperparameters
input_size = 1
hidden_size = 32
output_size = 1
learning_rate = 0.1
num_epochs = 1000

# Create random initial weights for input to hidden and hidden to output connections
w_ih = np.random.rand(input_size, hidden_size)
w_ho = np.random.rand(hidden_size, output_size)

# Initialize the hidden state
h_t = np.zeros((1, hidden_size))

# Define the input sequence
input_sequence = np.array([[0.1], [0.2], [0.3], [0.4], [0.5]])
target_sequence = np.array([[0.2], [0.4], [0.6], [0.8], [1.0]])

# Training loop
for epoch in range(num_epochs):
    total_loss = 0

    for t in range(len(input_sequence)):
        x_t = input_sequence[t:t+1]
        y_target = target_sequence[t:t+1]

        # Calculate the hidden state
        a_t = np.dot(x_t, w_ih) + np.dot(h_t, w_ho)
        h_t = sigmoid(a_t)
        
        # Calculate the output
        output_t = np.dot(h_t, w_ho)

        # Calculate the loss (mean squared error)
        loss = 0.5 * np.square(output_t - y_target).sum()
        total_loss += loss

        # Backpropagation (gradient descent)
        delta_output = output_t - y_target
        delta_h = np.dot(delta_output, w_ho.T)
        delta_a = delta_h * h_t * (1 - h_t)
        
        w_ho -= learning_rate * np.dot(h_t.T, delta_output)
        w_ih -= learning_rate * np.dot(x_t.T, delta_a)

    if (epoch + 1) % 100 == 0:
        print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {total_loss}")

# Testing the trained RNN
print("Testing the trained RNN:")
for t in range(len(input_sequence)):
    x_t = input_sequence[t:t+1]
    a_t = np.dot(x_t, w_ih) + np.dot(h_t, w_ho)
    h_t = sigmoid(a_t)
    output_t = np.dot(h_t, w_ho)
    print(f"Input: {x_t[0, 0]:.2f}, Predicted Output: {output_t[0, 0]:.2f}")
