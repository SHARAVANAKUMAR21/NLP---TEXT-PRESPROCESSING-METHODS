import spacy

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

# Example sentence
sentence = "This is an Simple sentence."

# Process the sentence with spaCy
doc = nlp(sentence)

# Filter out stopwords and punctuation
tokens_without_stopwords = [token.text for token in doc if not token.is_stop and not token.is_punct]

# Join tokens back into a sentence
filtered_sentence = ' '.join(tokens_without_stopwords)

print("Original Sentence:")
print(sentence)
print("\nFiltered Sentence:")
print(filtered_sentence)
