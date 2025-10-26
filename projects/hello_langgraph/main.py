from langgraph.graph import StateGraph, START, END
from typing import TypedDict    

class MyState(TypedDict):
    message: str
    name: str

def greet(state: MyState) -> MyState:
    """This is wish node

    Every node in langraph takes state as input and returns 
    state

    Args:
        state (MyState): State

    Returns:
        MyState: State
    """
    state['message'] = f"Hello, {state['name']}!"
    return state   

state_graph = StateGraph(MyState)

state_graph.add_node("wish",greet)
state_graph.add_edge(START,"wish")
state_graph.add_edge ("wish",END)

graph = state_graph.compile()


if __name__ == "__main__":
    main()
