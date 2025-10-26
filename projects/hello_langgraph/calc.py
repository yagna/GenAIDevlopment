from langgraph.graph import StateGraph,START, END
from typing import TypedDict

class Input(TypedDict):
    a: int
    b: int
    result: int|None

def perform_math(state: Input) -> input:
        state['result'] = state['a'] + state['b']
        return state


    
state_graph = StateGraph(Input)
state_graph.add_node("perform_math",perform_math)
state_graph.add_edge(START,"perform_math")
state_graph.add_edge("perform_math",END)


graph= state_graph.compile()