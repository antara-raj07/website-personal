from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from starlette.staticfiles import StaticFiles
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory=os.path.join('client', 'build', 'static')), name ="static")

@app.get("/api/health")
def read_data():
    return JSONResponse(content={"message": "Hello from the backend!"})

@app.get("/{full_path:path}")
def serve_react_app(full_path: str):
    if full_path == "":
        full_path = "index.html"
    return FileResponse(os.path.join('client', 'build', full_path))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)