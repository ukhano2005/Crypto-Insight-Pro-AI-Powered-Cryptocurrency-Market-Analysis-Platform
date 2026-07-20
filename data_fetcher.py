filepath: CryptoInsight-AI/agents/data_fetcher.py
from langchain_core.messages import AIMessage
from tools.alpha_vantage_tool import fetch_crypto_data
from agents.__init__ import AgentState

def data_fetcher_node(state: AgentState):
    coin = state["coin"]
    data = fetch_crypto_data(coin)
    
    if data["status"] == "success":
        msg = f"Successfully fetched data for {coin}. Latest Price: ${data['latest_price']:,.2f}, Volume: {data['volume']:.2f}"
    else:
        msg = f"Failed to fetch data: {data['message']}"
        
    return {"market_data": data, "messages": [AIMessage(content=msg, name="DataFetcher")]}
    