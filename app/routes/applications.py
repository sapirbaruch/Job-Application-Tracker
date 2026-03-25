from fastapi import APIRouter, HTTPException, status

from app.repository import ApplicationRepository
from app.schemas import (
    JobApplicationCreate,
    JobApplicationResponse,
    JobApplicationUpdate,
)

router = APIRouter(prefix="/applications", tags=["Applications"])
repository = ApplicationRepository()


@router.get("", response_model=list[JobApplicationResponse])
def list_applications() -> list[JobApplicationResponse]:
    return repository.list_all()


@router.get("/{application_id}", response_model=JobApplicationResponse)
def get_application(application_id: int) -> JobApplicationResponse:
    application = repository.get_by_id(application_id)
    if application is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found",
        )
    return application


@router.post(
    "",
    response_model=JobApplicationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_application(data: JobApplicationCreate) -> JobApplicationResponse:
    return repository.create(data)


@router.put("/{application_id}", response_model=JobApplicationResponse)
def update_application(
    application_id: int,
    data: JobApplicationUpdate,
) -> JobApplicationResponse:
    application = repository.update(application_id, data)
    if application is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found",
        )
    return application


@router.delete("/{application_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_application(application_id: int) -> None:
    deleted = repository.delete(application_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found",
        )