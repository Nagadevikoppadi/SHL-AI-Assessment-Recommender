from fastapi import FastAPI
from pydantic import BaseModel
from agent import recommend_assessments

app = FastAPI(title="SHL AI Assessment Recommender")


class JobRequest(BaseModel):
    description: str


@app.get("/")
def home():
    return {"message": "SHL AI Assessment Recommender is running!"}


@app.post("/recommend")
def recommend(request: JobRequest):
    results = recommend_assessments(request.description)
    return {"recommendations": results}