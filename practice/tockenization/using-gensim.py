from gensim.utils import simple_preprocess # type: ignore

# Your sentence
sentence = """Modi in Varanasi: Prime Minister Narendra Modi is set to visit his constituency of Varanasi today, on 18 June, for the first time since winning the seat in the 2024 Lok Sabha elections, which concluded earlier this month."""

# Tokenize the sentence using Gensim
tokens = simple_preprocess(sentence)

# Print the tokens
print(tokens)
