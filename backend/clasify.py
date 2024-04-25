from model import model_pipeline 
from fastapi import FastAPI, UploadFile
from typing import Union
from PIL import Image
import io
import sys

app = FastAPI()

print(sys.path)
@app.get("/")
def read_root():
    return {"Hello": "witam"}


@app.post("/ask/")
def ask(text: str, image: UploadFile):
    content = image.file.read()

    image = Image.open(io.BytesIO(content)).convert('RGB')
    #image = Image.open(image.file)
    result = model_pipeline(text,image)
    return result