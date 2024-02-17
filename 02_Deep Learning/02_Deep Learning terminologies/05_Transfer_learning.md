# Fine tuning in NNs
Fine-tuning is a specific type of transfer learning. It refers to the process of taking a pre-trained model and making adjustments to its weights and parameters to adapt it to a new, related task. Fine-tuning typically involves modifying the top layers of the model and training it on a new dataset. The pre-trained model's parameters are adjusted to better fit the new data, overcoming the challenges of limited data.

For eg, we can just take a really good open source model, and freeze everything except the last few layers. This can lead to performance superior to the one, if we had just trained our model.
