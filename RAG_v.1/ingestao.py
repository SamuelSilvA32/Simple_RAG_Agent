from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
from pathlib import Path

# ======================
# Configurações
# ======================
PERSIST_DIR = "./chroma_db"
COLLECTION_NAME = "base_conhecimento"
ARQUIVO_MD = "conhecimento.md"

# ======================
# Embeddings
# ======================
modelo_embedding = SentenceTransformer("all-MiniLM-L6-v2")

# ======================
# Banco vetorial
# ======================
client = chromadb.Client(
    Settings(
        persist_directory=PERSIST_DIR,
        is_persistent=True
    )
)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME
)

# ======================
# Ingestão
# ======================
def main():
    print("🔹 Iniciando ingestão do conhecimento...")

    texto = Path(ARQUIVO_MD).read_text(encoding="utf-8")

    embedding = modelo_embedding.encode(texto).tolist()

    collection.add(
        documents=[texto],
        ids=["conhecimento_principal"]
    )

    print("✅ Base de conhecimento atualizada com sucesso!")

if __name__ == "__main__":
    main()
