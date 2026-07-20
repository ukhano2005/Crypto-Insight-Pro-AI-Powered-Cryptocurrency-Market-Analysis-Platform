filepath: CryptoInsight-AI/agents/report_generator.py
from langchain_core.messages import AIMessage
from langchain_groq import ChatGroq
from config.config import PRIMARY_MODEL
from utils.prompts import REPORT_GENERATOR_PROMPT
from agents.__init__ import AgentState

def report_generator_node(state: AgentState):
    llm = ChatGroq(model_name=PRIMARY_MODEL, temperature=0.4)
    prompt = REPORT_GENERATOR_PROMPT.format(coin=state["coin"], language=state["language"])
    
    context = f"""
    Data: {state.get('market_data')}
    News: {state.get('news_data')}
    Tech Analysis: {state.get('tech_analysis')}
    """
    
    response = llm.invoke([
        {"role": "system", "content": prompt},
        {"role": "user", "content": f"Generate the final report using this context:\n{context}"}
    ])
    
    return {"final_report": response.content, "messages": [AIMessage(content="Report completed.", name="ReportGenerator")]}
    