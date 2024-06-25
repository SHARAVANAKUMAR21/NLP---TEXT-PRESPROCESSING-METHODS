import nltk
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Sentence to be lemmatized
sentence2 = "The cats are sitting on the mats"

# Tokenize the sentence
tokens = nltk.word_tokenize(sentence2)

# Initialize the WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# Lemmatize the tokens
lemmas = [lemmatizer.lemmatize(token) for token in tokens]

# Print the lemmas
print(lemmas)
