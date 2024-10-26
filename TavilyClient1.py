from tavily import TavilyClient
from langflow import Langflow
from langdetect import detect
from textblob import TextBlob

# Instanciando o cliente Tavily com a chave da API
tavily_client = TavilyClient(api_key="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")

# Instanciando o Langflow
langflow = Langflow()

# Função para detectar a linguagem da consulta
def detect_language(text):
    return detect(text)

# Função para traduzir a resposta para o idioma da consulta
def translate_response(response, target_language):
    blob = TextBlob(response)
    return str(blob.translate(to=target_language))

# Executando uma consulta de busca simples
query = "Quem é Leo Messi?"
response = tavily_client.search(query)

# Processando a resposta com Langflow
processed_response = langflow.process(response)

# Detectando a linguagem da consulta
query_language = detect_language(query)

# Traduzindo a resposta processada para o idioma da consulta
translated_response = translate_response(processed_response, query_language)

# Imprimindo a resposta processada e traduzida
print(f"Consulta: {query}")
print(f"Resposta: {translated_response}")
