from transformers import pipeline

chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")

prompt = "Hello! How are you?"

response = chatbot(prompt, max_length=50, pad_token_id=50256)

print(response[0]['generated_text'])