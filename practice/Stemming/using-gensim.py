import nltk
from nltk.stem import PorterStemmer
from gensim.utils import tokenize

# Download NLTK 'punkt' tokenizer models if not already downloaded
nltk.download('punkt')

# Sentence to be stemmed
sentence = "Running when raining"

# Tokenize the sentence using Gensim
tokens = list(tokenize(sentence))

# Initialize the PorterStemmer
porter = PorterStemmer()

# Stem the tokens
stems = [porter.stem(token) for token in tokens]

# Print the stems
print(stems)
