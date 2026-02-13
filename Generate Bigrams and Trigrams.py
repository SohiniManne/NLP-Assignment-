from nltk.util import ngrams
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')

text = "Natural language processing is fun"
tokens = word_tokenize(text)

# Bigrams
bigrams = list(ngrams(tokens, 2))
print("Bigrams:")
print(bigrams)

# Trigrams
trigrams = list(ngrams(tokens, 3))
print("\nTrigrams:")
print(trigrams)
