import nltk
from nltk.corpus import stopwords
from gensim.utils import simple_preprocess
from gensim.models.phrases import Phrases, Phraser

# Download NLTK stopwords data if not already downloaded
nltk.download('stopwords')

# Example sentence
sentence = "This is an Simple sentence."

# Tokenize the sentence into words
words = simple_preprocess(sentence, deacc=True)

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
