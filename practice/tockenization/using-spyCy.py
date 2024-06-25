import spacy

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

# Your sentence
sentence = """Modi in Varanasi: Prime Minister Narendra Modi is set to visit his constituency of Varanasi today, on 18 June, for the first time since winning the seat in the 2024 Lok Sabha elections, which concluded earlier this month."""

# Process the sentence with spaCy
doc = nlp(sentence)

# Extract and print tokens
tokens = [token.text for token in doc]
print(tokens)
