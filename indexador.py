from openai import OpenAI
from dotenv import load_dotenv
import os
import faiss
import numpy as np

# Carrega as variáveis do arquivo .env
load_dotenv()

# Inicialize o cliente da OpenAI com a chave do .env
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("A chave de API da OpenAI não está definida. Configure a variável OPENAI_API_KEY no arquivo .env.")
client = OpenAI(api_key=api_key)

# Função para gerar embedding de cada chunk
def gerar_embedding(texto):
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=texto
    )
    embedding = response.data[0].embedding
    return np.array(embedding, dtype='float32')

# Lendo os chunks
try:
    with open("documentos/church_history_eusebius.txt", "r", encoding="utf-8") as f:
        chunks = f.read().split("-----\n")
        chunks = [c.strip() for c in chunks if c.strip()]
except FileNotFoundError:
    raise FileNotFoundError("O arquivo 'documentos/church_history_eusebius.txt' não foi encontrado. Verifique o caminho.")

# Gerando embeddings
embeddings = []
for i, chunk in enumerate(chunks, 1):
    print(f"Processando chunk {i}/{len(chunks)}...")
    emb = gerar_embedding(chunk)
    embeddings.append(emb)

# Convertendo para numpy
embeddings = np.array(embeddings)

# Criando o indexador FAISS
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Salvando o index FAISS
faiss.write_index(index, "index.faiss")

# Salvando os chunks ordenados
with open("chunks_salvos.txt", "w", encoding="utf-8") as f:
    for chunk in chunks:
        f.write(chunk + "\n-----\n")

print("Indexação concluída com sucesso!")