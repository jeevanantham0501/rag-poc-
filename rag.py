from groq import Groq
import os
client = Groq(api_key="Your_api key")

# Load knowledge base
with open("data.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines()]

# Question (you can modify)
question = input("Enter your question: ")

# Keyword-based retrieval
keywords = question.lower().split()
matched = []

for line in lines:
    l = line.lower()
    if any(k in l for k in keywords):
        matched.append(line)

# Safe fallback
if not matched:
    matched.append("No relevant data found in knowledge base.")

context = "\n".join(matched)

prompt = f"""
Use ONLY the following context to answer the question.

Context:
{context}

Question:
{question}
"""

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": prompt}]
)

print("\n=== RAG Answer ===")
print(response.choices[0].message.content)
