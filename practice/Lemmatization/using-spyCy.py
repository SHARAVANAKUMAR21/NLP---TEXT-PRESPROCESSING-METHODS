import spacy

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

# Sentence to be lemmatized
sentence2 = "The cats are sitting on the mats"

# Process the sentence with spaCy
doc = nlp(sentence2)

# Extract and print lemmas
lemmas = [token.lemma_ for token in doc]
print(lemmas)
