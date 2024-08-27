import requests
from bs4 import BeautifulSoup

def duckduckgo_search(query):
    # Formata a URL para a pesquisa no DuckDuckGo
    url = f"https://html.duckduckgo.com/html?q={query}"
    
    # Faz a requisição HTTP para a URL
    response = requests.get(url)
    
    # Analisa o conteúdo HTML da página
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontra todos os links de resultados da pesquisa
    results = soup.find_all('a', class_='result__a')
    
    # Extrai os URLs dos resultados
    links = [result['href'] for result in results]
    
    return links

# Exemplo de uso:
query = "Python web scraping"
results = duckduckgo_search(query)

for idx, link in enumerate(results, 1):
    print(f"Result {idx}: {link}")
