import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sentence = "NLP makes machines understand human language"

tokens = word_tokenize(sentence)
pos_tags = pos_tag(tokens)

print("POS Tags:")
for word, tag in pos_tags:
    print(f"{word} -> {tag}")
