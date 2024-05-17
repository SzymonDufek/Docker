from fastapi import FastAPI, File, Form, UploadFile, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from PIL import Image
import io
import requests
from model import model_pipeline

app = FastAPI()



DATABASE_SERVICE_URL = "http://database_service:8001"

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/ask")
async def ask(text: str = Form(...), image: UploadFile = File(...)):
    try:
        content = await image.read()
        image = Image.open(io.BytesIO(content)).convert('RGB')
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid image file")

    result = model_pipeline(text, image)
    
    response = requests.post(
        f"{DATABASE_SERVICE_URL}/query_response/",
        json={"question": text, "response": result}
    )

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Database service error")
    
    return result


