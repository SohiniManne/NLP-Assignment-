from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "NLP is interesting",
    "NLP is powerful",
    "Machine learning and NLP"
]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

print("Feature Names:")
print(vectorizer.get_feature_names_out())

print("\nTF-IDF Matrix:")
print(tfidf_matrix.toarray())
