# **DuckDuckGobusca.py**

Este código realiza uma busca no DuckDuckGo e extrai os links dos resultados da pesquisa.

1. **Importações**:
  
  - `requests`: Faz requisições HTTP.
    
  - `BeautifulSoup` do `bs4`: Analisa e extrai dados do HTML.
    
2. **Função** `duckduckgo_search(query)`:
  
  - Formata a URL para a pesquisa no DuckDuckGo usando a query fornecida.
    
  - Faz uma requisição HTTP para a URL.
    
  - Analisa o conteúdo HTML da resposta usando BeautifulSoup.
    
  - Encontra todos os links de resultados da pesquisa.
    
  - Extrai e retorna os URLs dos resultados encontrados.
    
3. **Exemplo de Uso**:
  
  - Realiza uma busca por "Python web scraping".
    
  - Imprime os links dos resultados da pesquisa.
    

#### O que Instalar

Para usar este código, você precisa instalar as bibliotecas `requests` e `beautifulsoup4`. Você pode instalar estas bibliotecas usando o pip:

```
pip install requests
pip install beautifulsoup4
```

# 

# **DuckDuckGobusca1.py**

######

######

#### Descrição do Código

Este código utiliza o LangChain, uma biblioteca que integra diversas ferramentas de IA, para realizar uma busca no DuckDuckGo e retornar os resultados.

1. **Importação de Bibliotecas**:
  
  - `DuckDuckGoSearchRun` da `langchain_community.tools`: Ferramenta de busca que utiliza a API do DuckDuckGo para realizar pesquisas na web.
2. **Instanciação e Uso**:
  
  - `ddg_search = DuckDuckGoSearchRun()`: Cria uma instância do objeto de busca do DuckDuckGo.
    
  - `result = ddg_search.run("receita sabão?")`: Executa a busca pela query "receita sabão?" e armazena o resultado em `result`.
    
  - `print(result)`: Imprime os resultados da busca.
    

#### O que Instalar

Para usar este código, você precisa instalar as seguintes bibliotecas:

- `duckduckgo-search`
  
- `langchain`
  
- `langchain_community`
  

Você pode instalar todas as dependências usando pip:

```
pip install duckduckgo-search
pip install langchain
pip install langchain_community
```

#### Como Executar

1. **Instale as dependências**: Execute os comandos acima no terminal para instalar as bibliotecas necessárias.
  
2. **Escreva o código**: Copie e cole o código Python em um arquivo, por exemplo, `duckduckgo_search.py`.
  
3. **Execute o código**: No terminal, navegue até o diretório onde o arquivo `duckduckgo_search.py` está salvo e execute o seguinte comando:
  
  ```
  python 
  ```
  

# **busca_groq.py**

#### Descrição do Código

Este código Python usa a biblioteca Groq para interagir com um modelo de linguagem (LLM) e gerar uma resposta para uma pergunta fornecida.

1. **Importação de Bibliotecas**:
  
  - `os`: Utilizada para acessar variáveis de ambiente.
    
  - `Groq`: Biblioteca utilizada para interagir com o modelo de linguagem.
    
2. **Configuração da API**:
  
  - Obtém a chave da API da variável de ambiente `GROQ_API_KEY` e cria uma instância do cliente `Groq`.
3. **Criação da Solicitação de Chat**:
  
  - `client.chat.completions.create()`: Envia uma mensagem ao modelo de linguagem especificado (`llama3-8b-8192`) e solicita uma resposta para a query "receita para sabão simples".
4. **Impressão da Resposta**:
  
  - Imprime o conteúdo da resposta gerada pelo modelo.

#### O que Instalar

Para usar este código, você precisa instalar a biblioteca `groq`. Você pode instalá-la usando o pip:

```
pip install groq
```

#### Como Executar

1. **Instale a dependência**: Execute o comando acima no terminal para instalar a biblioteca `groq`.
  
2. **Configure a variável de ambiente**: Defina a chave da API como uma variável de ambiente no seu sistema operacional. Por exemplo, no Windows:
  
  ```
  setx GROQ_API_KEY "sua_chave_api_aqui"
  ```
  
3. **Escreva o código**: Copie e cole o código Python em um arquivo, por exemplo, `groq_search.py`.
  
4. **Execute o código**: No terminal, navegue até o diretório onde o arquivo `groq_search.py` está salvo e execute o seguinte comando:
  
  ```
  python 
  ```
  

# busca_groq.py

#### Descrição do Código

Este código Python utiliza a biblioteca Groq para interagir com um modelo de linguagem e gerar uma resposta para uma pergunta específica.

1. **Importação de Bibliotecas**:
  
  - `os`: Utilizada para acessar variáveis de ambiente.
    
  - `Groq`: Biblioteca utilizada para interagir com o modelo de linguagem.
    
2. **Configuração da API**:
  
  - A chave da API é obtida da variável de ambiente `GROQ_API_KEY`. Se a chave não for encontrada, o código levanta um erro.
3. **Inicializando o Cliente Groq**:
  
  - Cria uma instância do cliente `Groq` usando a chave da API.
4. **Função** `teste_groq()`:
  
  - Envia uma mensagem de teste para a IA perguntando "qual melhor sabão disponível no Brasil" e usa o modelo `llama3-8b-8192`.
    
  - Exibe a resposta da IA.
    
  - Em caso de erro, captura e exibe a mensagem de erro.
    
5. **Chamada da Função**:
  
  - Chama a função `teste_groq()` para executar o código.

#### O que Instalar

Para usar este código, você precisa instalar a biblioteca `groq`. Você pode instalá-la usando o pip:

```
pip install groq
```

#### Como Executar

1. **Instale a dependência**: Execute o comando acima no terminal para instalar a biblioteca `groq`.
  
2. **Configure a variável de ambiente**: Defina a chave da API como uma variável de ambiente no seu sistema operacional. Por exemplo, no Windows:
  
  ```
  setx GROQ_API_KEY "sua_chave_api_aqui"
  ```
  
3. **Escreva o código**: Copie e cole o código Python em um arquivo, por exemplo, `groq_test.py`.
  
4. **Execute o código**: No terminal, navegue até o diretório onde o arquivo `groq_test.py` está salvo e execute o seguinte comando:
  
  ```
  python groq_test.py
  
  ```
  

# busca_groq_v1.py

#### Descrição do Código

Este código Python utiliza a biblioteca Groq para interagir com um modelo de linguagem e gerar uma resposta para uma pergunta fornecida.

1. **Importação de Bibliotecas**:
  
  - `os`: Utilizada para acessar variáveis de ambiente.
    
  - `Groq`: Biblioteca utilizada para interagir com o modelo de linguagem.
    
2. **Configuração da API**:
  
  - Obtém a chave da API da variável de ambiente `GROQ_API_KEY` e cria uma instância do cliente `Groq`.
3. **Criação da Solicitação de Chat**:
  
  - `client.chat.completions.create()`: Envia uma mensagem ao modelo de linguagem especificado (`llama3-8b-8192`) e solicita uma resposta para a query "receita para sabão simples".
4. **Impressão da Resposta**:
  
  - Imprime o conteúdo da resposta gerada pelo modelo.

#### O que Instalar

Para usar este código, você precisa instalar a biblioteca `groq`. Você pode instalá-la usando o pip:

```
pip install groq
```

#### Como Executar

1. **Instale a dependência**: Execute o comando acima no terminal para instalar a biblioteca `groq`.
  
2. **Configure a variável de ambiente**: Defina a chave da API como uma variável de ambiente no seu sistema operacional. Por exemplo, no Windows:
  
  ```
  setx GROQ_API_KEY "sua_chave_api_aqui"
  ```
  
3. **Escreva o código**: Copie e cole o código Python em um arquivo, por exemplo, `groq_search.py`.
  
4. **Execute o código**: No terminal, navegue até o diretório onde o arquivo `groq_search.py` está salvo e execute o seguinte comando:
  
  ```
  python groq_search.py
  
  ```
  

# wikipedia.py

#### Descrição do Código

Este código Python utiliza a biblioteca LangChain para fazer consultas na Wikipedia e retornar resultados.

1. **Importação de Bibliotecas**:
  
  - `WikipediaQueryRun` da `langchain_community.tools`: Ferramenta para realizar consultas na Wikipedia.
    
  - `WikipediaAPIWrapper` da `langchain_community.utilities`: Envolve a API da Wikipedia para facilitar seu uso.
    
2. **Instanciação e Configuração**:
  
  - `WikipediaAPIWrapper()`: Cria uma instância do wrapper da API da Wikipedia.
    
  - `WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())`: Cria uma instância da ferramenta de consulta, configurada para usar a API da Wikipedia.
    
3. **Execução da Consulta**:
  
  - `wikipedia.run("Palmeiras?")`: Faz uma consulta na Wikipedia sobre "Palmeiras" e retorna os resultados.
4. **Impressão do Resultado**:
  
  - `print()`: Imprime o resultado da consulta no console.

#### O que Instalar

Para usar este código, você precisa instalar as seguintes bibliotecas:

- `langchain`
  
- `langchain_community`
  

Você pode instalar todas as dependências usando pip:

```
pip install langchain
pip install langchain_community
```

#### Como Executar

1. **Instale as dependências**: Execute os comandos acima no terminal para instalar as bibliotecas `langchain` e `langchain_community`.
  
2. **Escreva o código**: Copie e cole o código Python em um arquivo, por exemplo, `wikipedia_search.py`.
  
3. **Execute o código**: No terminal, navegue até o diretório onde o arquivo `wikipedia_search.py` está salvo e execute o seguinte comando:
  
  python wikipedia_search.py
  

# youtube.py

#### Descrição do Código

Este código Python utiliza a biblioteca LangChain para realizar buscas no YouTube.

1. **Importação de Bibliotecas**:
  
  - `YouTubeSearchTool` da `langchain_community.tools`: Ferramenta para realizar buscas no YouTube.
2. **Instanciação e Configuração**:
  
  - `YouTubeSearchTool()`: Cria uma instância da ferramenta de busca no YouTube.

#### O que Instalar

Para usar este código, você precisa instalar a biblioteca `youtube_search` e `langchain_community`. Você pode instalá-las usando pip:

```
pip install --upgrade --quiet youtube_search
pip install langchain
pip install langchain_community
```

#### Como Executar

1. **Instale as dependências**: Execute os comandos acima no terminal para instalar as bibliotecas necessárias.
  
2. **Escreva o código**: Copie e cole o código Python em um arquivo, por exemplo, `youtube_search.py`.
  
3. **Execute o código**: No terminal, navegue até o diretório onde o arquivo `youtube_search.py` está salvo e execute o seguinte comando:
  
  ```
  python youtube_search.py
  
  ```
