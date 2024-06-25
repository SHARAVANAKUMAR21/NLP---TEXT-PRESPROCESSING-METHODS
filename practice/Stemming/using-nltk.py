#Stemming
import nltk

from nltk.stem import PorterStemmer


sentence1 = "Running when raining"


# Tokenize the sentence
tokens = nltk.word_tokenize(sentence1)

# Initialize the PorterStemmer
porter = PorterStemmer()

# Stem the tokens
stems = [porter.stem(token) for token in tokens]

print(stems)
