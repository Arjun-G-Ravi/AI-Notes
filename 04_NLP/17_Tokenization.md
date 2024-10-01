# Tokenizers
Tokenizers convert text(or pretty much any form of data) into tokens, which can be easily used by the model.

![alt text](image-21.png)

# Basic Tokenization Algorithm - SentencePiece
SentencePiece is an unsupervised text tokenizer and detokenizer primarily used in Natural Language Processing (NLP) tasks. 
It converts text into subwords or tokens for model training and inference. 
Developed by Google, it is a language-agnostic, character-level tokenizer and can handle texts without relying on predefined vocabulary or language-specific rules.

Common subword tokenizers in transformers are:
- Byte-Pair Encoding [BPE]
- WordPiece
- Unigram