import nltk

nltk.download('punkt')


sentence = """Modi in Varanasi: Prime Minister Narendra Modi is set to visit his constituency of Varanasi today, on 18 June, for the first time since winning the seat in the 2024 Lok Sabha elections, which concluded earlier this month."""

tokens = nltk.word_tokenize(sentence)

print(tokens)
