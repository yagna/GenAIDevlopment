from dotenv import load_dotenv
import os
from history import graph,HistoryStateByDate
from langgraph.graph import START, END, StateGraph


def main():
    print(os.getenv('LANGSMITH_MYKEY', 'NO KEY FOUND'))
    load_dotenv()
    print(os.getenv('LANGSMITH_MYKEY','NO KEY FOUND'))
    state = HistoryStateByDate(
       
           date='14-aug-1947',
           desc=''
       
   )
    response = graph.invoke(state)
    print(response['desc'])



if __name__ == "__main__":
    main()
