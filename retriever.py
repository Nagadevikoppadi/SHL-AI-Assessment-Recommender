import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("vector_db/catalog.index")

with open("vector_db/catalog.pkl", "rb") as f:
    catalog = pickle.load(f)


def retrieve(query, k=3):
    query_embedding = model.encode([query]).astype("float32")
    distances, indices = index.search(query_embedding, k)

    results = []
    for idx in indices[0]:
        if idx < len(catalog):
            results.append(catalog[idx])

    return results