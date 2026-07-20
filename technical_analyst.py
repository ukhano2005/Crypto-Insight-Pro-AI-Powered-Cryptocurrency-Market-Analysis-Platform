filepath: CryptoInsight-AI/agents/technical_analyst.py
from langchain_core.messages import AIMessage
from langchain_groq import ChatGroq
from config.config import PRIMARY_MODEL
from utils.prompts import TECH_ANALYST_PROMPT
from agents.__init__ import AgentState

def technical_analyst_node(state: AgentState):
    llm = ChatGroq(model_name=PRIMARY_MODEL, temperature=0.2)
    prompt = TECH_ANALYST_PROMPT.format(coin=state["coin"])
    
    raw_data = state.get("market_data", {}).get("latest_price", "No data")
    
    response = llm.invoke([
        {"role": "system", "content": prompt},
        {"role": "user", "content": f"Analyze this data point: Current Price ${raw_data}"}
    ])
    
    return {"tech_analysis": response.content, "messages": [AIMessage(content=response.content, name="TechAnalyst")]}
    