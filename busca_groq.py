import os
from groq import Groq

# Configuração da chave API
api_key = os.environ.get("GROQ_API_KEY")

if not api_key:
    raise ValueError("A chave da API não foi encontrada. Certifique-se de que a variável de ambiente 'GROQ_API_KEY' está definida.")

# Inicializando o cliente Groq
client = Groq(api_key=api_key)

def teste_groq():
    try:
        # Enviando uma mensagem de teste para a IA
        chat_completion = client.chat.completions.create(
            messages=[
                { "role": "user",
                  "content": "qual melhor sabão disponivel no brasil" }
            ],
            model="llama3-8b-8192",
        )
        
        # Exibindo a resposta da IA
        print(chat_completion.choices[0].message.content)
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Chamar a função para testar
teste_groq()
