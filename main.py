from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Define o template do prompt
template = """
Você é um assistente visual. 
Responda apenas em Português.

input: {input}
"""

# Criação do PromptTemplate
base_prompt = PromptTemplate(input_variables=["input"], template=template)

# Instancia o modelo ChatGroq
llm = ChatGroq(model_name='llama3-8b-8192')

# Criação da memória de conversa
memory = ConversationBufferMemory(memory_key='chat_history', input_key='input')

# Configuração do LLMChain com o modelo, o prompt e a memória
llm_chain = LLMChain(llm=llm, prompt=base_prompt, memory=memory)

# Inicializar histórico de conversação
conversation_history = []

# Loop para entrada contínua do usuário
def main():
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["sair", "exit", "quit"]:
            break
        
        # Adicionar entrada do usuário ao histórico
        conversation_history.append(f"Você: {user_input}")
        
        try:
            # Gerar resposta do chatbot
            response = llm_chain.run(input=user_input)
            conversation_history.append(f"Chatbot: {response}")
        except Exception as e:
            conversation_history.append(f"Erro: {e}")
        
        # Exibir histórico da conversa
        print("\nHistórico da Conversa:\n")
        for message in conversation_history:
            print(message)

if __name__ == "__main__":
    main()
