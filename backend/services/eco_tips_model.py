from transformers import pipeline

tip_gen = pipeline("text2text-generation", model="google/flan-t5-large")

def generate_eco_tips(topic: str) -> str:
    prompt = f"Give 3 practical eco-friendly tips about {topic}"
    result = tip_gen(prompt, max_new_tokens=100)
    return result[0]["generated_text"]
