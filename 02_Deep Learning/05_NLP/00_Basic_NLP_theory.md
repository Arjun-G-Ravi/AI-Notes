# Basic NLP

## Text normalization
Text normalization in Natural Language Processing (NLP) refers to the process of converting a piece of text into a standardized form. This involves correcting spelling errors, expanding abbreviations and contractions, removing punctuation marks, converting all characters to lowercase or uppercase, and applying other transformations that make the text easier to analyze and compare.

## Tokenisation
Converting text data into tokens.
- Should "New York" be considered as one token or two? Should punctuations be considered to be separate tokens? etc. all depends on the application. 

## Stemming
Reducing words to their base or root form, by chopping off parts of words.
Eg: SnowBallStemmer(violent stemmer), PorterStemmer(simple stemmer)

## Lemmatization
It is stemming performed by consulting the context of the text

## Regular Expression
Formally, a regular expression is an algebraic notation for characterizing a set of strings. Regular expressions are particularly useful for searching in texts, when we have a pattern to search for and a corpus of texts to search through.
- To perform regex, we can use the 're' library in python.

# Edit distance
Edit distance gives us a way to quantify both of these intuitions about string similarity. More formally, the minimum edit distance between two strings is defined as the minimum number of editing operations (operations like insertion, deletion, substitution) needed to transform one string into another.
