import os
import re

# Função básica de limpeza do texto (remove linhas vazias e espaços desnecessários)
def limpar_texto(texto):
    texto = re.sub(r'\n+', '\n', texto)  # Remove múltiplas quebras de linha
    texto = texto.strip()
    return texto

# Função para dividir o texto em chunks de aproximadamente 1000 palavras
def dividir_em_chunks(texto, tamanho_chunk=1000):
    palavras = texto.split()
    chunks = []
    for i in range(0, len(palavras), tamanho_chunk):
        chunk = ' '.join(palavras[i:i + tamanho_chunk])
        chunks.append(chunk)
    return chunks

# Lê o arquivo original
with open("documentos/church_history_eusebius.txt", "r", encoding="utf-8") as f:
    texto_original = f.read()

# Limpa o texto
texto_limpo = limpar_texto(texto_original)

# Divide em chunks
chunks = dividir_em_chunks(texto_limpo, tamanho_chunk=1000)

# Salva os chunks no arquivo chunks.txt
with open("chunks.txt", "w", encoding="utf-8") as f:
    for chunk in chunks:
        f.write(chunk + "\n-----\n")

print(f"Processamento concluído! {len(chunks)} chunks criados.")
