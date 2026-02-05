
# Sanskrit Document Retrieval-Augmented Generation (RAG) System

This project implements a **CPU-only Retrieval-Augmented Generation (RAG) system** for answering questions from **Sanskrit documents**.  
The system ingests Sanskrit text, indexes it using vector embeddings, retrieves relevant context, and returns **grounded, non-hallucinatory answers**.

Due to limitations of lightweight CPU-based language models for Sanskrit generation, the system uses an **extractive RAG approach**, selecting the most relevant Sanskrit sentence from retrieved context.

---

## Features

- Sanskrit document ingestion (`.txt`, `.pdf`, `.docx`)
- Sanskrit-aware preprocessing and chunking
- Vector-based retrieval using **FAISS**
- CPU-only inference (no GPU required)
- Deterministic extractive answering (no hallucination)
- Modular RAG architecture (Retriever + Answering)

---

##  Project Structure

```

RAG_Sanskrit_Adinath/
│
├── code/
│   ├── ingest.py
│   ├── preprocess.py
│   ├── build_index.py
│   ├── retriever.py
│   ├── answer_extractor.py
│   └── query.py
│
├── data/
│   └── Rag-docs.docx
│
├── report/
│   └── Sanskrit_RAG_Report.pdf
│
├── requirements.txt
├── .gitignore
└── README.md

````

---

## ⚙️ Setup Instructions

### Create virtual environment
```bash
python -m venv venv
````

Activate:

* **Windows**

```bash
venv\Scripts\activate
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Build vector index

```bash
cd code
python build_index.py
```

---

### Run query interface

```bash
python query.py
```

---

## Example Query

```
शंखनादः किम् आनयितुम् गच्छति?
```

### Example Output

```
ततः शंखनादः आपणम् गच्छति, शर्कराम् जीर्णे वस्त्रे न्यस्यति च।
```

---

## 🧠 Design Notes

* Retrieval is performed using **multilingual sentence embeddings**
* FAISS is used for efficient similarity search
* Final answer is **extracted directly from retrieved Sanskrit context**
* This ensures accuracy and avoids hallucination

---

## ⚠️ Limitations

* Sanskrit generation quality depends on extractive context
* Designed for **CPU-only environments**
* Not intended for free-form Sanskrit text generation

---

## Evaluation Alignment

This implementation satisfies:

* End-to-end RAG architecture
* CPU-only constraint
* Sanskrit document handling
* Modular, reproducible code
* Clear and defensible technical design

---

## Author

**Adinath Nage**

