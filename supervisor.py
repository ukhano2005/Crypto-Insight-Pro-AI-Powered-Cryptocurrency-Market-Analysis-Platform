filepath: CryptoInsight-AI/agents/supervisor.py
from langgraph.graph import StateGraph, END
from agents.__init__ import AgentState
from agents.data_fetcher import data_fetcher_node
from agents.news_researcher import news_researcher_node
from agents.technical_analyst import technical_analyst_node
from agents.report_generator import report_generator_node
from langchain_core.messages import AIMessage

def supervisor_node(state: AgentState):
    # Simple deterministic routing for predictable UI loading
    if not state.get("market_data"):
        return {"next_step": "data_fetcher"}
    elif not state.get("news_data"):
        return {"next_step": "news_researcher"}
    elif not state.get("tech_analysis"):
        return {"next_step": "technical_analyst"}
    elif not state.get("final_report"):
        return {"next_step": "report_generator"}
    else:
        return {"next_step": END}

def build_graph():
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("supervisor", supervisor_node)
    workflow.add_node("data_fetcher", data_fetcher_node)
    workflow.add_node("news_researcher", news_researcher_node)
    workflow.add_node("technical_analyst", technical_analyst_node)
    workflow.add_node("report_generator", report_generator_node)
    
    # Add edges
    workflow.set_entry_point("supervisor")
    
    # Edges from workers back to supervisor
    for node in ["data_fetcher", "news_researcher", "technical_analyst", "report_generator"]:
        workflow.add_edge(node, "supervisor")
        
    # Conditional routing from supervisor
    workflow.add_conditional_edges(
        "supervisor",
        lambda state: state["next_step"],
        {
            "data_fetcher": "data_fetcher",
            "news_researcher": "news_researcher",
            "technical_analyst": "technical_analyst",
            "report_generator": "report_generator",
            END: END
        }
    )
    
    return workflow.compile()
    