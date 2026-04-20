from transformers import RobertaTokenizer, RobertaForSequenceClassification
import torch

tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
model = RobertaForSequenceClassification.from_pretrained('roberta-base')

text = "This is amazing!"
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

outputs = model(**inputs)
logits = outputs.logits

probs = torch.softmax(logits, dim=1)
print(probs)