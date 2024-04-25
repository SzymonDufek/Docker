FROM tiangolo/uvicorn-gunicorn:python3.10-slim

WORKDIR /frontend

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /app/uploads

EXPOSE 80

CMD ["python", "app.py"]