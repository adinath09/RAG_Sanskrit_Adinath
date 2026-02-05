import faiss
import pickle
from sentence_transformers import SentenceTransformer
import numpy as np

MODEL_NAME = "intfloat/multilingual-e5-small"

index = faiss.read_index("sanskrit.index")

with open("chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

model = SentenceTransformer(MODEL_NAME)

def retrieve(query, k=2):
    q_emb = model.encode([query])
    D, I = index.search(np.array(q_emb), k)
    return [chunks[i] for i in I[0]]
