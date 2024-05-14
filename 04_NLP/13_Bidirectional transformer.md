# Bidirectional Transformers
It is a modification to transformers that use a self-attention mechanism to allow the model to attend to both the past and the future context when processing a word.

`BERT` was the first widely successful bidirectional Transformer-based language model. It built upon the Transformer architecture and used a novel pre-training approach to learn bidirectional representations.

They were made primarily used for masked word prediction and sentence continuity prediction. But once trained, they can be finetuned for tasks like sentence classification, POS-tagging and even text generation(not autoregressive text-generation). In-fact, it is really good at those tasks.

## Need
Transformers are fine in many autoregressive tasks like summarization and machine translation. But when tackling problems like sequence classification, it is essential to have information about all the tokens(past and future) for every token. Bidirectional encoders overcome this limitation by allowing the self-attention mechanism to range over the entire input.(No attention masks.)

![alt text](<Screenshot from 2024-04-28 10-56-51.png>)

```
The key architecture difference is in bidirectional models we don’t mask the future tokens during training. This means the model has access to the full context which makes the sentence structure very clear. 

The tradeoff is that this architecture cannot be used for real-time, auto-regressive text generation, since the model requires the full input sequence to make predictions.
```

# Training
Training is done by predicting randomly masked words and next sentence prediction. (Explained better with BERT section, coming next.)