from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
        title="hello Library",
        summary="getting started with fastapi",
        version="0.1.0"

    )

class SuccessMessage(BaseModel):
    Message: str

@app.get("/",response_model=SuccessMessage)
async def greet():
     return {"Message":"Hello World"}


#if __name__ == "__main__":
#    main()
