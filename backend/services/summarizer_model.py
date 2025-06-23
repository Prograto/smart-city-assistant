from transformers import pipeline

# Load summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text: str) -> str:
    summary = summarizer(text, max_length=200, min_length=60, do_sample=False)
    return summary[0]["summary_text"]
