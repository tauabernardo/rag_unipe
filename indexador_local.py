import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Carrega o modelo local de embeddings
modelo = SentenceTransformer('all-MiniLM-L6-v2')

# Lê os chunks
with open("chunks_pt.txt", "r", encoding="utf-8") as f:
    chunks = f.read().split("-----\n")
    chunks = [c.strip() for c in chunks if c.strip()]

# Gera embeddings normalizados (melhor para FAISS + L2)
embeddings = modelo.encode(chunks, convert_to_numpy=True, normalize_embeddings=True)

# Cria e salva o index FAISS
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)
faiss.write_index(index, "index.faiss")

# Salva os chunks
with open("chunks_salvos.txt", "w", encoding="utf-8") as f:
    for chunk in chunks:
        f.write(chunk + "\n-----\n")

print("✅ Indexação concluída com sucesso!")
