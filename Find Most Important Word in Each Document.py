from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

documents = [
    "Natural language processing is amazing",
    "Language models process text",
    "Text processing and NLP"
]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

feature_names = vectorizer.get_feature_names_out()

for i, doc in enumerate(tfidf_matrix.toarray()):
    top_index = np.argmax(doc)
    print(f"Document {i+1} Most Important Word:",
          feature_names[top_index])
