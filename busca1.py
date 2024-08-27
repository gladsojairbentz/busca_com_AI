from langchain_community.tools import DuckDuckGoSearchRun
ddg_search = DuckDuckGoSearchRun()
result = ddg_search.run("receita sabão?")
print(result)
# pip install duckduckgo-search
# pip install langchain
# pip install langchain_community
