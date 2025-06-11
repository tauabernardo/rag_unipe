from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Chave de API não encontrada no .env")
client = OpenAI(api_key=api_key)

try:
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input="Teste simples"
    )
    print("Sucesso:", response.data[0].embedding[:10])
except Exception as e:
    print("Erro:", str(e))