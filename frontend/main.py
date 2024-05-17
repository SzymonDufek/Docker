from fastapi import FastAPI, Form, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import requests

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

BACKEND_SERVICE_URL = "http://backend:9000"

@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("static/index.html") as f:
        return HTMLResponse(content=f.read())

@app.post("/ask")
async def ask(text: str = Form(...), image: UploadFile = File(...)):
    try:
        response = requests.post(
            f"{BACKEND_SERVICE_URL}/ask",
            data={"text": text},
            files={"image": image.file}
        )

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Backend service error")
        
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
