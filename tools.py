import os
from langchain_core.tools import tool
from tavily import TavilyClient

# Opcjonalnie: Jeśli nie masz klucza Tavily, ustaw to na True, aby użyć fałszywych danych (dla demo)
USE_MOCK_DATA = False

@tool
def web_search(query: str):
    """
    Useful for searching the internet for current events, competitor news, 
    and market data. Input should be a search query.
    """
    if USE_MOCK_DATA:
        # Fallback for demo purposes if API keys are missing
        return f"Mock search results for {query}: Competitor X released a new AI feature yesterday. Pricing increased by 10%."
    
    try:
        api_key = os.getenv("TAVILY_API_KEY")
        if not api_key:
            return "Error: TAVILY_API_KEY not found."
            
        client = TavilyClient(api_key=api_key)
        response = client.search(query, search_depth="advanced")
        
        # Format results contextually
        context = "\n".join(
            [f"- {obj['content']} (Source: {obj['url']})" for obj in response['results']]
        )
        return context
    except Exception as e:
        return f"Error performing search: {e}"
