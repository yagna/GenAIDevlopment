from typing import Union

from fastapi import FastAPI

app = FastAPI(
        title="hello Library",
        summary="getting started with fastapi",
        version="0.1.0"

    )

@app.get("/")
def greet() -> str:
     return {"Hello": "World"}


#if __name__ == "__main__":
#    main()
