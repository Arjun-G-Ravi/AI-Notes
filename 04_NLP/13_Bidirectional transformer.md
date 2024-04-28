# Bidirectional Transformers
It is a modification to transformers that use a self-attention mechanism to allow the model to attend to both the past and the future context when processing a word.

- They are primarilllly used for masked prediction, POS-tagging, etc., but can also be extended to text generation.

# Need
Transformers are fine in many autoregressive tasks like summarization and machine translation. But when takling problems like sequence classification, it is essential to have information about all the tokens(past and future) for every token.Bidirectional encoders overcome this limitation by allowing the self-attention mechanism to range over the entire input.

![alt text](<Screenshot from 2024-04-28 10-56-51.png>)
