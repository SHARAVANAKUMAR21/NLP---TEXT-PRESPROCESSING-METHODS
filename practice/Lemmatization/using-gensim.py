from gensim.utils import simple_preprocess
from gensim.models.phrases import Phrases, Phraser

# Sample sentences
sentences = [
    "Modi in Varanasi: Prime Minister Narendra Modi is set to visit his constituency of Varanasi today, on 18 June, for the first time since winning the seat in the 2024 Lok Sabha elections, which concluded earlier this month.",
    "The cats are sitting on the mats"
]

# Tokenize the sentences
tokenized_sentences = [simple_preprocess(sentence) for sentence in sentences]

print("Tokenized sentences:")
for tokens in tokenized_sentences:
    print(tokens)

# Generate bigrams
phrases = Phrases(tokenized_sentences, min_count=1, threshold=1)
bigram = Phraser(phrases)

print("\nBigrams:")
for tokens in tokenized_sentences:
    print(bigram[tokens])
