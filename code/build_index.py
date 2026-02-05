import numpy as np
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from preprocess import normalize_text, chunk_sanskrit
from ingest import load_document

MODEL_NAME = "intfloat/multilingual-e5-small"

def build_index():
    text = load_document(r"..\data\Rag-docs.docx")
    text = normalize_text(text)
    chunks = chunk_sanskrit(text)

    model = SentenceTransformer(MODEL_NAME)
    embeddings = model.encode(chunks)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))

    faiss.write_index(index, "sanskrit.index")

    with open("chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

    print("Index built with", len(chunks), "chunks")

if __name__ == "__main__":
    build_index()
