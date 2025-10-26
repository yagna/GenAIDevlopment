from dotenv import load_dotenv
import os
from langchain.

def main():
    print(os.getenv('LANGSMITH_MYKEY', 'NO KEY FOUND'))
    load_dotenv()
    print(os.getenv('LANGSMITH_MYKEY','NO KEY FOUND'))
    state = (
        draft='we will provide the date as input and coud you please get the history even for the date.',
        tone='formal'
    )
    response = graph.invoke(state)
    print(response['mail'])



if __name__ == "__main__":
    main()
