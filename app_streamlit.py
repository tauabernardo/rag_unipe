import faiss
import numpy as np
import streamlit as st
from sentence_transformers import SentenceTransformer

# Carrega o modelo de embeddings
modelo = SentenceTransformer('all-MiniLM-L6-v2')

# Carrega index FAISS e os chunks
index = faiss.read_index("index.faiss")

with open("chunks_pt.txt", "r", encoding="utf-8") as f:
    chunks = f.read().split("-----\n")
    chunks = [c.strip() for c in chunks if c.strip()]

# Função de busca com distâncias
def buscar_resposta(pergunta, k=3):
    emb_pergunta = modelo.encode([pergunta], convert_to_numpy=True, normalize_embeddings=True)
    D, I = index.search(emb_pergunta, k)
    resultados = [(chunks[i], D[0][j]) for j, i in enumerate(I[0])]
    return resultados

# Interface Streamlit
st.set_page_config(page_title="RAG - História da Igreja", layout="wide")
st.title("📜 Sistema de Consulta - História da Igreja (RAG Local)")
st.markdown("Digite uma pergunta relacionada ao conteúdo histórico-teológico.")

pergunta = st.text_input("🧠 Sua pergunta:")

if st.button("🔎 Consultar"):
    if pergunta:
        resultados = buscar_resposta(pergunta)
        for i, (trecho, distancia) in enumerate(resultados):
            st.write(f"**Trecho {i+1}** (🔍 Distância: `{distancia:.4f}`):")
            st.code(trecho[:1500] + ("..." if len(trecho) > 1500 else ""), language="markdown")
            st.write("---")
    else:
        st.warning("❗ Por favor, digite uma pergunta.")
