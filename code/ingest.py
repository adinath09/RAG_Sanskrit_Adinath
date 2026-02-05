from pypdf import PdfReader
from docx import Document
import os

def load_txt(path):
    with open(path, encoding="utf-8-sig", errors="ignore") as f:
        return f.read()

def load_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

def load_docx(path):
    doc = Document(path)
    return "\n".join(p.text for p in doc.paragraphs)

def load_document(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    ext = os.path.splitext(path)[1].lower()

    if ext == ".txt":
        return load_txt(path)
    elif ext == ".pdf":
        return load_pdf(path)
    elif ext == ".docx":
        return load_docx(path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")

if __name__ == "__main__":
    doc_path = r"..\data\Rag-docs.docx"
    text = load_document(doc_path)

    print("Document loaded successfully")
    print("Character count:", len(text))
