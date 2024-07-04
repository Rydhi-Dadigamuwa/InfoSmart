from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarization_fn(text, min_lenght=20, max_length=30, do_sample=False):
    return summarizer(text, min_length=min_lenght, max_length=max_length, do_sample=False)[0]['summary_text']


