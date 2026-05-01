from transformers import pipeline

summarizer = pipeline("summarization")

text = """Artificial Intelligence is transforming industries by automating tasks,
improving decision-making, and enabling new innovations across sectors."""

summary = summarizer(text, max_length=30, min_length=10, do_sample=False)

print(summary[0]['summary_text'])