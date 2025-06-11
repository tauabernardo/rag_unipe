import faiss
import numpy as np
import streamlit as st
from sentence_transformers import SentenceTransformer

# Carrega o modelo local de embeddings
modelo = SentenceTransformer('all-MiniLM-L6-v2')

# Carrega o index FAISS
index = faiss.read_index("index.faiss")

# Carrega os chunks salvos
with open("chunks_pt.txt", "r", encoding="utf-8") as f:
    chunks = f.read().split("-----\n")
    chunks = [c.strip() for c in chunks if c.strip()]

# Função de busca
def buscar_resposta(pergunta, k=3):
    emb_pergunta = modelo.encode([pergunta], convert_to_numpy=True)
    D, I = index.search(emb_pergunta, k)
    resultados = [chunks[i] for i in I[0]]
    return resultados

# Streamlit interface
st.title("Sistema de Consulta - História da Igreja (RAG Local)")
pergunta = st.text_input("Digite sua pergunta:")

if st.button("Consultar"):
    if pergunta:
        resultados = buscar_resposta(pergunta)
        for i, trecho in enumerate(resultados):
            st.write(f"**Trecho {i+1}:**")
            st.write(trecho)
            st.write("---")
    else:
        st.warning("Digite uma pergunta para consultar.")
