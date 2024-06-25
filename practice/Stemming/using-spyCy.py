import spacy

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

# Sentence to be lemmatized
sentence1 = "Running when raining"

# Process the sentence with spaCy
doc = nlp(sentence1)

# Extract and print lemmas
lemmas = [token.lemma_ for token in doc]

print(lemmas)
