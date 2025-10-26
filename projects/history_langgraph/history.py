from typing import TypedDict
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import START, END, StateGraph
import os

class HistoryState(TypedDict):
    event: str
    date: str
    desc: str

load_dotenv()
model_name = os.getenv('MODEL_NAME')
model_provider = os.getenv('MODEL_PROVIDER')
llm = init_chat_model(model=model_name, model_provider=model_provider)



def historic_events_by_date(state: HistoryState) -> HistoryState:
    desc = state['desc']
    date = state['date']
    event = state['event']
    
    prompt = ChatPromptTemplate([
        ('system', 'You are an expert Historian  good with date'),
        ("user", f"Consider the following date  {date} find 10 historic events on date step by step"),
        ("user", f"List down all the events  {event}")
    ])
    chain = prompt | llm 
    response = chain.invoke({'desc': desc, 'event': event})
    state['desc'] = response.content
    return state

toner_graph = StateGraph(HistoryState)
toner_graph.add_node("historic_events_by_date", historic_events_by_date)
toner_graph.add_edge(START, "historic_events_by_date")
toner_graph.add_edge("historic_events_by_date", END)

graph = toner_graph.compile()