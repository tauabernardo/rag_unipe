from deep_translator import GoogleTranslator
import textwrap

# Lê os chunks em inglês
with open("chunks.txt", "r", encoding="utf-8") as f:
    chunks = f.read().split("-----\n")
    chunks = [c.strip() for c in chunks if c.strip()]

# Função para dividir em subchunks menores de 4500 caracteres
def dividir_subchunks(texto, tamanho=4500):
    return textwrap.wrap(texto, tamanho)

# Traduz e salva
with open("chunks_pt.txt", "w", encoding="utf-8") as f:
    for i, chunk in enumerate(chunks):
        print(f"Traduzindo chunk {i+1}/{len(chunks)}...")
        subchunks = dividir_subchunks(chunk)
        traducao_total = ""
        for subchunk in subchunks:
            traducao_parcial = GoogleTranslator(source='auto', target='pt').translate(subchunk)
            traducao_total += traducao_parcial + " "
        f.write(traducao_total.strip() + "\n-----\n")

print("Tradução concluída com sucesso!")
