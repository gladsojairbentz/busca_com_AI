import os

from groq import Groq
#chave na variavel de ambiente do windows 
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "receita para sabão simples",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)
