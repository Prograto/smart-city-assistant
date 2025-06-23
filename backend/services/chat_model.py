from transformers import pipeline

# Load the model (Zephyr or Flan-T5 — use Flan if memory is low)
chat_pipeline = pipeline("text-generation", model="google/flan-t5-large", max_length=200)

def generate_chat_response(prompt: str) -> str:
    result = chat_pipeline(prompt)
    return result[0]["generated_text"]
