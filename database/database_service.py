# database/database_service.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import List

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class QueryResponse(Base):
    __tablename__ = "query_responses"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, index=True)
    response = Column(Text)

Base.metadata.create_all(bind=engine)

app = FastAPI()

class QueryResponseCreate(BaseModel):
    question: str
    response: str

class QueryResponseRead(BaseModel):
    id: int
    question: str
    response: str

@app.post("/query_response/", response_model=QueryResponseCreate)
def create_query_response(query_response: QueryResponseCreate):
    db = SessionLocal()
    db_query_response = QueryResponse(**query_response.dict())
    db.add(db_query_response)
    db.commit()
    db.refresh(db_query_response)
    db.close()
    return db_query_response

@app.get("/query_responses/", response_model=List[QueryResponseRead])
def read_query_responses():
    db = SessionLocal()
    responses = db.query(QueryResponse).all()
    db.close()
    return responses

@app.get("/", response_model=List[QueryResponseRead])
def read_index():
    db = SessionLocal()
    responses = db.query(QueryResponse).all()
    db.close()
    return responses
