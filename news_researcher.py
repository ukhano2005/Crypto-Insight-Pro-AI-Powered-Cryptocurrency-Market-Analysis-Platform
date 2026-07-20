filepath: CryptoInsight-AI/agents/news_researcher.py
from langchain_core.messages import AIMessage
from tools.search_tool import search_crypto_news
from agents.__init__ import AgentState

def news_researcher_node(state: AgentState):
    coin = state["coin"]
    news = search_crypto_news(coin)
    
    msg = f"Gathered recent news for {coin}:\n{news[:200]}..."
    return {"news_data": news, "messages": [AIMessage(content=msg, name="NewsResearcher")]}
    