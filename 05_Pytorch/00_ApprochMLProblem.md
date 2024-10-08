# Whenever using ML to solve a problem:

0) Import, dataset and dataloaders creation, device definition
1) Design the model (the forward pass), Define input and output sizes
2) Construct loss and the optimiser
3) Training loop
     - Forward pass: Compute prediction [inference]
     - Compute loss for accuracy check
     - Backward pass: Calculate gradients wrt loss
     - Update weights
4) Predict output and calculate accuracy (use torch.no_grad())