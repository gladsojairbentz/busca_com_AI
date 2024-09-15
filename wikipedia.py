from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

wikipedia = WikipediaQueryRun(api_wrapper=piWikipediaAPIWrapper())

print(wikipedia.run("Palmeiras?"))