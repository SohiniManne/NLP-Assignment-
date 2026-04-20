import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense, Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

# Sample data
texts = ["I love this", "I hate this", "This is great", "This is bad"]
labels = [1, 0, 1, 0]

# Tokenization
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
X = tokenizer.texts_to_sequences(texts)
X = pad_sequences(X, maxlen=5)

y = np.array(labels)

# Model
model = Sequential([
    Embedding(input_dim=1000, output_dim=32, input_length=5),
    SimpleRNN(32),
    Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=5)

# Prediction
print(model.predict(X))