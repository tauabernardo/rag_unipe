from deep_translator import GoogleTranslator

# Lê os chunks em inglês
with open("chunks.txt", "r", encoding="utf-8") as f:
    chunks = f.read().split("-----\n")
    chunks = [c.strip() for c in chunks if c.strip()]

# Traduz e salva
with open("chunks_pt.txt", "w", encoding="utf-8") as f:
    for i, chunk in enumerate(chunks):
        print(f"Traduzindo chunk {i+1}/{len(chunks)}...")
        traducao = GoogleTranslator(source='auto', target='pt').translate(chunk)
        f.write(traducao + "\n-----\n")

print("Tradução concluída com sucesso!")
