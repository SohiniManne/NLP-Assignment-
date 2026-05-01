from transformers import pipeline

qa_pipeline = pipeline("question-answering")

context = "The Taj Mahal is located in Agra, India."
question = "Where is the Taj Mahal located?"

result = qa_pipeline(question=question, context=context)

print(result["answer"])