# RAG POC (Python + Groq)

This is a simple **Retrieval-Augmented Generation (RAG)** Proof of Concept built using:
- Python
- Groq LLM API
- Text file as a mini-database (data.txt)

The project demonstrates how to:
1. Load text data
2. Retrieve relevant lines using a search method
3. Use an LLM to answer questions based on retrieved context

---

## 🚀 How It Works

### 1️⃣ **Retrieval**
The script searches the `data.txt` file and finds lines related to the question.

### 2️⃣ **Augmented Generation**
The relevant text is sent to Groq LLM to generate an accurate answer.

---

## 📁 Project Structure

```
rag-poc/
│── rag.py        # Main RAG script
│── data.txt      # Knowledge base (text document)
│── README.md     # Project documentation
```

---

## 🧪 Example Code (rag.py)

```python
from groq import Groq

API_KEY = "YOUR_GROQ_API_KEY"
client = Groq(api_key=API_KEY)

# Load the text document
with open("data.txt", "r") as f:
    lines = f.readlines()

question = "What is Python used for?"

# Simple retrieval
context = [line for line in lines if "Python" in line]
context_text = "\n".join(context)

prompt = f"""
Use only the following context to answer:

Context:
{context_text}

Question:
{question}
"""

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": prompt}]
)

print("\nAnswer:")
print(response.choices[0].message.content)
```

---

## ▶️ How to Run

### 1. Install dependencies
```
pip install groq
```

### 2. Add your API key
Replace:
```
API_KEY = "YOUR_GROQ_API_KEY"
```

### 3. Run the script
```
python rag.py
```

---

## 📦 Uses
- Learning RAG concepts
- Mini personal chatbot over a document
- POC for interviews or GitHub portfolio project

---

## ⭐ Future Improvements
- Use embeddings for better retrieval  
- Add a GUI or a simple FastAPI server  
- Upload multiple documents  

---

## ✨ Author
Jeevanantham S
