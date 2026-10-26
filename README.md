# Chatbot Conversacional com LangChain e Groq

Aplicação interativa de chatbot em linha de comando desenvolvida em Python, utilizando o framework **LangChain** integrado aos modelos de inferência de ultra-baixa latência da **Groq**.

---

## 🛠️ Tecnologias
- **Python 3.10+**
- **LangChain** (Orquestração de prompts e memória de contexto)
- **Groq API** (Inferência de LLM)
- **python-dotenv** (Gestão de variáveis de ambiente)

---

## 🚀 Como Executar

### 1. Clonar o repositório
```bash
git clone https://github.com/RicsonRamos/conversational-chatbot-langchain.git
cd conversational-chatbot-langchain
```

### 2. Configurar o ambiente
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Configurar credenciais
Copie o arquivo de exemplo e insira sua chave da Groq:
```bash
cp .env.example .env
```
Edite o arquivo `.env`:
```dotenv
GROQ_API_KEY=sua_chave_groq_aqui
```

### 4. Executar
```bash
python main.py
```

Para encerrar a conversa a qualquer momento, digite `sair` ou `exit`.

---

## 📄 Licença
Distribuído sob licença MIT. Veja [LICENSE](LICENSE) para mais informações.
