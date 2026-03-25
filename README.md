# Job Application Tracker

A simple FastAPI backend service for managing job applications.

This project was developed as part of EX1 and demonstrates a clean and minimal REST API using FastAPI, Pydantic, and pytest.

---

##  Features

- Create a job application
- List all job applications
- Get a job application by ID
- Update a job application
- Delete a job application

---

## Tech Stack

- Python 3.11+
- FastAPI
- Pydantic
- Uvicorn
- pytest

---

## Project Structure

├── app/
│ ├── init.py
│ ├── main.py # FastAPI app entry point
│ ├── schemas.py # Pydantic models
│ ├── repository.py # In-memory data layer
│ └── routes/
│ ├── init.py
│ └── applications.py # API routes
├── tests/
│ └── test_applications.py # API tests
├── pyproject.toml
├── README.md
└── .gitignore



---

##  Setup

### 1. Create virtual environment

```bash
uv venv
source .venv/bin/activate
uv sync --dev
```

## Running the API

Start the server:

```bash
uv run uvicorn app.main:app --reload
```

The API will be available at:

API: http://127.0.0.1:8000

Docs (Swagger): http://127.0.0.1:8000/docs

