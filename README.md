# SHL AI Assessment Recommender

## Overview

This project recommends SHL assessments based on a job description using semantic search with Sentence Transformers and FAISS. Users can submit a job description through a FastAPI API and receive the most relevant SHL assessments.

## Features

- Semantic search using Sentence Transformers
- FAISS vector database for fast similarity search
- FastAPI REST API
- Swagger UI for API testing
- GitHub-ready project structure

## Tech Stack

- Python 3.13
- FastAPI
- Sentence Transformers
- FAISS
- NumPy
- Pydantic
- Uvicorn

## Project Structure

```
SHL-AI-Assessment-Recommender/
│
├── app.py
├── agent.py
├── retriever.py
├── embeddings.py
├── models.py
├── prompts.py
├── catalog.json
├── requirements.txt
├── README.md
├── vector_db/
└── data/
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Nagadevikoppadi/SHL-AI-Assessment-Recommender.git
cd SHL-AI-Assessment-Recommender
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Generate Embeddings

```bash
python embeddings.py
```

## Run the API

```bash
python -m uvicorn app:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

## API Endpoint

### POST /recommend

Example Request

```json
{
  "description": "Looking for a software engineer with Python, SQL and problem solving skills"
}
```

Example Response

```json
{
  "recommendations": [
    {
      "name": "OPQ32",
      "description": "Occupational Personality Questionnaire",
      "category": "Behavioral",
      "test_type": "Personality",
      "url": "https://www.shl.com/"
    }
  ]
}
```

## Technologies Used

- FastAPI
- Sentence Transformers
- FAISS
- NumPy
- Pydantic
- Uvicorn
- Git

## Author

Nagadevi Koppadi
