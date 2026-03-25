from fastapi import APIRouter, HTTPException, status

# Import repository (data layer)
from app.repository import ApplicationRepository

# Import Pydantic schemas for request/response validation
from app.schemas import (
    JobApplicationCreate,
    JobApplicationResponse,
    JobApplicationUpdate,
)

# Create router for all /applications endpoints
router = APIRouter(prefix="/applications", tags=["Applications"])

# In-memory data storage (shared across all routes)
repository = ApplicationRepository()


# Get all job applications
@router.get("", response_model=list[JobApplicationResponse])
def list_applications() -> list[JobApplicationResponse]:
    return repository.list_all()


# Get a specific application by ID
@router.get("/{application_id}", response_model=JobApplicationResponse)
def get_application(application_id: int) -> JobApplicationResponse:
    application = repository.get_by_id(application_id)

    # Return 404 if application not found
    if application is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found",
        )

    return application


# Create a new job application
@router.post(
    "",
    response_model=JobApplicationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_application(data: JobApplicationCreate) -> JobApplicationResponse:
    return repository.create(data)


# Update an existing application
@router.put("/{application_id}", response_model=JobApplicationResponse)
def update_application(
    application_id: int,
    data: JobApplicationUpdate,
) -> JobApplicationResponse:
    application = repository.update(application_id, data)

    # Return 404 if application does not exist
    if application is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found",
        )

    return application


# Delete an application by ID
@router.delete("/{application_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_application(application_id: int) -> None:
    deleted = repository.delete(application_id)

    # Return 404 if application does not exist
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found",
        )