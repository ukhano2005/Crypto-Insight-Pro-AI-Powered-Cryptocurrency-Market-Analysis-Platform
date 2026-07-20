filepath: CryptoInsight-AI/agents/__init__.py
from typing import TypedDict, Annotated, Sequence
import operator
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    coin: str
    language: str
    market_data: dict
    news_data: str
    tech_analysis: str
    final_report: str
    next_step: str
    