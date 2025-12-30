from rag import responder

def main():
    print("🤖 Agente RAG — Ficha de Curiosidades")
    print("Digite 'sair' para encerrar.\n")

    while True:
        pergunta = input("❓ Pergunta: ").strip()

        if pergunta.lower() in ["sair", "exit", "quit"]:
            print("👋 Encerrando.")
            break

        resposta = responder(pergunta)
        print("\n💡 Resposta:")
        print(resposta)
        print("-" * 50)

if __name__ == "__main__":
    main()
