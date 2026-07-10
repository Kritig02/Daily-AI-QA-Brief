import os

from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

client = TavilyClient(api_key= os.getenv("TAVILY_API_KEY"))

def get_latest_news():

    response = client.search(query="""Find the latest AI & Quality Engineering news. 
        Focus on AI agents, Playwright, Selenium, test automation, LLM testing, MCP, and AI developer tools. 
        Prefer TestGuild, Software Testing Weekly, Playwright Blog, Selenium Blog, Ministry of Testing, and InfoQ. 
        Return the top 5 articles with title, source, link, and why it matters to QA engineers.""", search_depth = "advanced", max_results=5)
    
    return response["results"]