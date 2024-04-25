FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN curl https://sh.rustup.rs -sSf | bash -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "clasify:app", "--host", "0.0.0.0", "--port", "8000"]