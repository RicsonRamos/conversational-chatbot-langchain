# Conversational Chatbot with LangChain and Groq LPU

Command-line conversational agent built with Python, LangChain, and Groq's high-speed inference engine for ultra-low-latency natural language dialogue with contextual memory.

---

## 1. Problema de Negócio e Contexto

No desenvolvimento de interfaces conversacionais e agentes de suporte em linha de comando (CLI), dois gargalos técnicos comuns comprometem a usabilidade e a experiência do usuário:

1. **Latência de Inferência Proibitiva:** Provedores de nuvem convencionais frequentemente apresentam latências de primeiro token (Time to First Token - TTFT) elevadas, inviabilizando fluxos conversacionais fluidos diretamente no terminal.
2. **Amnésia Contextual:** Implementações ingênuas de chamadas a APIs de LLM não preservam o histórico dos turnos anteriores, forçando o usuário a reenviar o contexto completo a cada iteração.

Este projeto foi construído para fornecer um cliente de diálogo interativo em terminal que:
- Mantém o encadeamento histórico contínuo da conversa por meio de estruturas formais de memória.
- Utiliza hardware especializado de processamento neural para entrega imediata de respostas em Português.
- Segue padrões estritos de segurança no isolamento de credenciais de API.

---

## 2. Processo e Racional das Escolhas Técnicas

### 2.1. Inferência com Groq LPU vs. Provedores Convencionais
- **Taxa de Geração de Tokens:** A escolha da API da Groq (executando o modelo `llama3-8b-8192` sobre unidades LPU - *Language Processing Units*) proporciona taxas de geração de centenas de tokens por segundo, eliminando tempos de espera perceptíveis no terminal.
- **Eficiência de Custo e Performance:** Para aplicações CLI de triagem e assistência ágil, o modelo Llama 3 8B oferece o equilíbrio ideal entre precisão linguística, capacidade de raciocínio e custo operacional.

### 2.2. Gestão de Estado com LangChain ConversationBufferMemory
- **Preservação de Contexto:** Em vez de concatenar manualmente strings no loop principal, utilizou-se o `ConversationBufferMemory` integrado ao `LLMChain`. Essa abordagem abstrai o gerenciamento de chaves de input/output e desacopla a lógica de retenção de memória da lógica de apresentação no terminal.
- **Segurança e Higiene de Código:** Todas as chaves e segredos de autenticação são estritamente isolados fora do versionamento de código via `python-dotenv` e `.env.example`, prevenindo incidentes de vazamento em repositórios públicos.

---

## 3. Resultados Atingidos e Métricas de Validação

### 3.1. Eficiência Operacional
- **Tempo de Resposta Sub-Segundo:** Respostas conversacionais completas entregues em frações de segundo, viabilizando uso interativo contínuo sem quebras de fluxo.
- **Coerência em Diálogos Multiturnos:** Manutenção consistente do contexto ao longo de dezenas de turnos de perguntas e respostas sequenciais sem perda da instrução de sistema (respostas em Português).

---

## 4. Arquitetura da Solução e Estrutura

```text
conversational-chatbot-langchain/
├── main.py              # Ponto de entrada, loop de execução CLI e orquestração do LLMChain
├── requirements.txt     # Dependências (langchain, langchain-groq, python-dotenv)
├── .env.example         # Template seguro para variáveis de ambiente
├── .gitignore           # Exclusão preventiva de arquivos locais (.env, .venv, caches)
└── LICENSE              # Licença de uso de software (MIT)
```

---

## 5. Como Executar

### 5.1. Pré-requisitos
- Python 3.10 ou superior
- Chave de API ativa da [Groq Cloud](https://console.groq.com)

### 5.2. Instalação e Configuração

1. Clone o repositório:
```bash
git clone https://github.com/RicsonRamos/conversational-chatbot-langchain.git
cd conversational-chatbot-langchain
```

2. Crie e ative um ambiente virtual:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure a chave de acesso:
```bash
cp .env.example .env
```
Edite o arquivo `.env` e atribua sua chave:
```dotenv
GROQ_API_KEY=gsk_sua_chave_groq_aqui
```

5. Inicie o chatbot no terminal:
```bash
python main.py
```
Para encerrar a sessão a qualquer momento, digite `sair`, `exit` ou `quit`.
