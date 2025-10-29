from typing import TypedDict
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import START, END, StateGraph
import os

class HistoryStateByDate(TypedDict):
    date: str
    desc: str

load_dotenv()
model_name = os.getenv('MODEL_NAME')
model_provider = os.getenv('MODEL_PROVIDER')
llm = init_chat_model(model=model_name, model_provider=model_provider)



def historic_events_by_date(state: HistoryStateByDate) -> HistoryStateByDate:
    desc = state['desc']
    date = state['date']
    
    prompt = ChatPromptTemplate([
        ('system', 'You are a historian good with dates'),
        ("user", "Given the  {date} "),
        ("user", "Find atleast 10 historic events which signify the date")
    ])
    chain = prompt | llm 
    response = chain.invoke({'date': date})
    state['desc'] = response.content
    return state

history_graph = StateGraph(HistoryStateByDate)
history_graph.add_node("historic_events_by_date", historic_events_by_date)
history_graph.add_edge(START, "historic_events_by_date")
history_graph.add_edge("historic_events_by_date", END)

graph = history_graph.compile()
