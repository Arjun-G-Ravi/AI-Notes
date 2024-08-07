# NLP
Natural Language Processing is a field of study focused on the interaction between computers and human (natural) languages. The ultimate objective of NLP is to read, decipher, understand, and make sense of the human language in a valuable way.

# NLP Pipeline
## 1. Data Acquisition
- Collect data from various sources
- If not directly available, you can web scrape or do surveys
- Nowadays, you can even use LLMs to create data

## 2. Text cleaning
- Using regex to extract only necessary sections
- Correcting spelling mistakes

## 3. Text preprocessing 
- `Tokenisation:`Converting text data into tokens. Should "New York" be considered as one token or two? Should punctuations be considered to be separate tokens? etc. all depends on the application. 

- `Lower casing`: To reduce randomness. Most words mean the same after lower casing. Exception: 'us' and 'US', etc.

- `Stemming:` Reducing words to their base or root form, by chopping off parts of words.
Eg: SnowBallStemmer(violent stemmer), PorterStemmer(simple stemmer)

- `Lemmatisation:` It is stemming performed by consulting the context of the text.

- `Text normalisation:` It is the process of converting a piece of text into a standardized form. This involves correcting spelling errors, expanding abbreviations and contractions, removing punctuation marks, converting all characters to lowercase or uppercase, and applying other transformations that make the text easier to analyze and compare.

- `Sequence Labelling: `Sequence labeling is a fundamental task  where the goal is to assign labels to each word in a given sequence of text. Eg: POS tagging, NER 
  - `POS tagging:`Parts of speech tagging is done to tag the parts of speech in a sentence.
  - `Named Entity recognition:` Named entity recognition is done to find out proper nouns like names, location, etc. which are usually not found in the vocabulory. Eg: Tony, Mumbai
- `Relationship extraction`: Sequence labelling and relationship extraction plays a pivotal role in it.
- `Coreference resolution`

## 4. Feature Enginnering
- Lets us extract meaningful information from raw data. This will empower the model to learn more from the same data
- Better data -> Better model

## 5. Model Building
NLP models comes in three types:
1. `Heuristic model` 
   - Rule based
   - good with small data
   - Can be difficult to come up with rules
2. `ML based model`
   - With a moderately large dataset
3. `Deep learning based model`
   - With huge datasets
   - Use RNNs, LSTMs, Transformers   

- `Ensemble` and `stacking` of models can almost always lead to better performing models

## 6. Evaluation
- Very hard
- Can be intristic or extensic. Explained in language models section.

## 7. Deployment
- Cloud services can be used
  
## 8. Monitoring and updating
- Update model with recent data
- Remove model's mistakes and biases