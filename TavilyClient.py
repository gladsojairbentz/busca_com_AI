from tavily import TavilyClient

# Instanciando o cliente Tavily com a chave da API
tavily_client = TavilyClient(api_key="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")

# Executando uma consulta de busca simples
query = "Quem é Leo Messi?"
response = tavily_client.search(query)

# Imprimindo a resposta da busca
print(response)
