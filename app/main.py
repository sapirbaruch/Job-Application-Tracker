from fastapi import FastAPI

# Import router that contains all application-related endpoints
from app.routes.applications import router as applications_router

# Create FastAPI application instance
app = FastAPI(title="Job Application Tracker API")


# Root endpoint to verify the API is running
@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Job Application Tracker API is running"}


# Register application routes under the main app
app.include_router(applications_router)