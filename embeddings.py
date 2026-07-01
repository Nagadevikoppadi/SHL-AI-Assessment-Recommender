import json
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

# Load catalog
with open("catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create searchable text
texts = [
    f"{item['name']} {item['description']} {item['category']} {item['test_type']}"
    for item in catalog
]

# Generate embeddings
print(texts)
print(len(texts))
embeddings = model.encode(texts)
embeddings = np.array(embeddings, dtype="float32")

print("Embeddings shape:", embeddings.shape)

if embeddings.ndim == 1:
    embeddings = embeddings.reshape(1, -1)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save index
faiss.write_index(index, "vector_db/catalog.index")

# Save catalog mapping
with open("vector_db/catalog.pkl", "wb") as f:
    pickle.dump(catalog, f)

print("Embeddings created successfully!")