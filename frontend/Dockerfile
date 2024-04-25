FROM tiangolo/uvicorn-gunicorn:python3.10-slim


RUN pip install --no-cache-dir -r /tmp/requirements.txt


RUN mkdir -p /app/uploads

RUN pip install requests

EXPOSE 80