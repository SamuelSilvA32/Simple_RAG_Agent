import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
from groq import Groq

# ======================
# Configurações
# ======================
load_dotenv()

PERSIST_DIR = "./chroma_db"
COLLECTION_NAME = "base_conhecimento"

MODELOS_GROQ = [
    "llama-3.1-8b-instant",
    "mixtral-8x7b-32768",
    "gemma2-9b-it",
]

# ======================
# Embeddings
# ======================
modelo_embedding = SentenceTransformer("all-MiniLM-L6-v2")

# ======================
# Banco Vetorial
# ======================
client_db = chromadb.Client(
    Settings(
        persist_directory=PERSIST_DIR,
        is_persistent=True
    )
)

collection = client_db.get_or_create_collection(
    name=COLLECTION_NAME
)

# ======================
# LLM
# ======================
client_llm = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ======================
# Função principal
# ======================
def responder(pergunta: str) -> str:
    embedding = modelo_embedding.encode(pergunta).tolist()

    resultados = collection.query(
        query_embeddings=[embedding],
        n_results=3
    )

    documentos = resultados.get("documents", [[]])[0]

    if not documentos:
        return "Não encontrei nenhuma informação relacionada a isso no documento."

    contexto = "\n".join(documentos)

    prompt = f"""
Você é um agente RAG **estritamente fiel ao CONTEXTO**.

REGRAS OBRIGATÓRIAS:
- Responda SOMENTE com base no CONTEXTO.
- NÃO use conhecimento externo.
- NÃO infira, complete ou suponha informações.
- Se a resposta não estiver no CONTEXTO, diga claramente que não possui essa informação.
- Você pode ser levemente criativo APENAS na forma de negar, nunca no conteúdo.

CONTEXTO:
{contexto}

PERGUNTA:
{pergunta}

RESPOSTA:
"""

    for modelo in MODELOS_GROQ:
        try:
            resposta = client_llm.chat.completions.create(
                model=modelo,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0,
            )
            return resposta.choices[0].message.content.strip()

        except Exception as e:
            erro = str(e)
            if "model_not_found" in erro or "decommissioned" in erro:
                continue
            return f"Erro ao consultar o modelo: {e}"

    return "Nenhum modelo Groq disponível no momento."
