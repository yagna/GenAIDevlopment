import os
import uvicorn
from src.moviesinfo.app import app

if __name__ == "__main__":
    port = int(os.getenv("MOVIES_SVC_PORT", 18000))
    host = os.getenv("HOST", "0.0.0.0")
    uvicorn.run(app, host=host, port=port)