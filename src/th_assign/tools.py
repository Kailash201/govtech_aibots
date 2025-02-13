from langchain_core.tools import tool
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools.pubmed.tool import PubmedQueryRun
from langchain_community.utilities import ArxivAPIWrapper
from langchain_community.tools import DuckDuckGoSearchRun

@tool
def wikipedia_tool(search: str):
    "Use this to know about any topic"
    wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    res = wikipedia.run(search)
    return res

@tool
def pubmed_tool(search: str):
    "Use this to know about any medical related topic"
    tool = PubmedQueryRun()
    res = tool.invoke(search)
    return res

@tool
def arxiv_tool(search: str):
    "Use this to know techincal and scientific topics"
    arxiv = ArxivAPIWrapper()
    docs = arxiv.run(search)
    print(type(docs))
    return docs

@tool
def ddg_search_tool(search: str):
    "Use this to do a general web search"
    search = DuckDuckGoSearchRun()
    res = search.invoke("Obama's first name?")
    return res


