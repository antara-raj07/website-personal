from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from starlette.staticfiles import StaticFiles
import os

app = FastAPI()



@app.get("/api/health")
def read_data():
    return JSONResponse(content={"message": "Hello from the backend!"})

@app.get("/")
def serve_react_app():
    return FileResponse("index.html")

app.mount("/", StaticFiles(directory="."), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)