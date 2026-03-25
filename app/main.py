from fastapi import FastAPI

from app.routes.applications import router as applications_router

app = FastAPI(title="Job Application Tracker API")


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Job Application Tracker API is running"}


app.include_router(applications_router)