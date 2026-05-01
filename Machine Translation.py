from transformers import pipeline

translator = pipeline("translation_en_to_fr")

text = "Machine learning is amazing."

translation = translator(text)

print(translation[0]['translation_text'])