import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

sentence = "This is an Simple sentence."

# Example sentence
nltk.download('stopwords')

# Tokenize the sentence into words
words = word_tokenize(sentence)

# Load English stopwords from NLTK
stop_words = set(stopwords.words('english'))

# Remove stopwords
filtered_words = [word for word in words if word.lower() not in stop_words]

# Join filtered words back into a sentence
filtered_sentence = ' '.join(filtered_words)

print("Original Sentence:")
print(sentence)
print("\nFiltered Sentence:")
print(filtered_sentence)