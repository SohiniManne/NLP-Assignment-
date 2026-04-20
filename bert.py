from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Load pretrained model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

# Input text
text = "I love this product!"
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

# Prediction
outputs = model(**inputs)
logits = outputs.logits

# Convert to probabilities
probs = torch.softmax(logits, dim=1)
print(probs)