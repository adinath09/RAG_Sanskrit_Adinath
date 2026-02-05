from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=False)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

def generate_answer(context, question):
    prompt = f"""
You are a question answering system.
Extract the EXACT answer phrase from the context.
Do not explain. Do not rephrase.

Context:
{context}

Question:
{question}

Answer (copy directly from context):
"""

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    outputs = model.generate(
        **inputs,
        max_length=200,
        do_sample=False
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
