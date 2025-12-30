[README.md](https://github.com/user-attachments/files/24384813/README.md)
# 🤖 Projeto RAG — Ficha de Curiosidades

Este projeto implementa um **RAG (Retrieval-Augmented Generation)** simples, auditável e fiel ao contexto, com foco **exclusivo nos conceitos técnicos**

---

## 🎯 Objetivo do Projeto

Demonstrar, de forma clara e didática:

* ingestão de conhecimento em formato Markdown;
* geração de embeddings locais;
* armazenamento em banco vetorial (ChromaDB);
* recuperação de contexto relevante;
* geração de respostas condicionadas **estritamente** ao contexto recuperado.

Este projeto foi deliberadamente mantido **simples e transparente** para fins educacionais e de validação conceitual.

---

## 🧠 Conceito Central: RAG Fiel ao Contexto

O agente **não pode**:

* usar conhecimento externo;
* inferir dados não declarados;
* completar lacunas automaticamente.

Se a informação **não estiver no documento**, o agente deve recusar a resposta de forma honesta.

Esse comportamento é intencional e faz parte do experimento.

---

## 📄 Base de Conhecimento

A base de conhecimento está no arquivo:

```
conhecimento.md
```

Ele contém uma **Ficha de Curiosidades** sobre o autor do projeto.

* qualquer informação fora do documento indica **falha no RAG**;

---

## 🗂️ Estrutura do Projeto

```
RAG_v.1/
├─ chroma_db/           # Banco vetorial persistido
├─ conhecimento.md      # Base de conhecimento
├─ ingestao.py          # Script de ingestão e indexação
├─ rag.py               # Lógica de recuperação + geração
├─ main.py              # Interface CLI simples
├─ .env                 # Variáveis de ambiente (API Key)
├─ requirements.txt
└─ README.md
```

---

## ⚙️ Tecnologias Utilizadas

* **Python 3.11+**
* **ChromaDB** — banco de dados vetorial
* **Sentence-Transformers** — geração de embeddings
* **Groq API** — LLM (LLaMA / Mixtral / Gemma)
* **dotenv** — gerenciamento de variáveis sensíveis

---

## 🔐 Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
GROQ_API_KEY=sua_chave_aqui
```

---

## ▶️ Como Executar

### 1️⃣ Criar ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

### 2️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 3️⃣ Atualizar a base vetorial (obrigatório)

Sempre que o `conhecimento.md` for alterado:

```bash
python ingestao.py
```

### 4️⃣ Iniciar o agente

```bash
python main.py
```

---

## 🧪 Exemplos de Perguntas para Validação

### ✅ Deve responder

* Qual é o nome completo do Samuel?
* Qual é a formação dele?
* Quais músicas ele prefere?

### ❌ Deve recusar

* Qual é a idade dele?
* Onde ele trabalha?
* Qual o nome dos pais?

Se o agente responder corretamente às negativas, o **RAG está funcionando como esperado**.

---


## 📜 Licença

Este projeto é distribuído sob a licença **MIT**, exclusivamente para fins educacionais e de aprendizado.

---

## 🧠 Nota Final

Este projeto marca a conclusão bem-sucedida da criação de um RAG funcional.
