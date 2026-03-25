from datetime import date
from enum import Enum

from pydantic import BaseModel, Field


class ApplicationStatus(str, Enum):
    saved = "saved"
    applied = "applied"
    interview = "interview"
    offer = "offer"
    rejected = "rejected"


class JobApplicationBase(BaseModel):
    company: str = Field(..., min_length=1, max_length=100)
    position: str = Field(..., min_length=1, max_length=100)
    status: ApplicationStatus
    location: str | None = Field(default=None, max_length=100)
    applied_date: date | None = None
    source: str | None = Field(default=None, max_length=100)
    notes: str | None = Field(default=None, max_length=500)
    favorite: bool = False


class JobApplicationCreate(JobApplicationBase):
    pass


class JobApplicationUpdate(JobApplicationBase):
    pass


class JobApplicationResponse(JobApplicationBase):
    id: int