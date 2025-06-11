import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Carrega o modelo local de embeddings
modelo = SentenceTransformer('all-MiniLM-L6-v2')

# Lendo os chunks
with open("chunks_pt.txt", "r", encoding="utf-8") as f:
    chunks = f.read().split("-----\n")
    chunks = [c.strip() for c in chunks if c.strip()]

# Gerando embeddings locais
embeddings = modelo.encode(chunks, convert_to_numpy=True)

# Criando o index FAISS
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Salvando o index FAISS
faiss.write_index(index, "index.faiss")

# Salvando os chunks ordenados
with open("chunks_salvos.txt", "w", encoding="utf-8") as f:
    for chunk in chunks:
        f.write(chunk + "\n-----\n")

print("Indexação local concluída com sucesso!")
