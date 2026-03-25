from datetime import date
from enum import Enum

from pydantic import BaseModel, Field


# Enum representing possible application statuses
class ApplicationStatus(str, Enum):
    saved = "saved"
    applied = "applied"
    interview = "interview"
    offer = "offer"
    rejected = "rejected"


# Base schema with shared fields for all operations
class JobApplicationBase(BaseModel):
    # Required fields with validation constraints
    company: str = Field(..., min_length=1, max_length=100)
    position: str = Field(..., min_length=1, max_length=100)

    # Enum ensures only valid status values are accepted
    status: ApplicationStatus

    # Optional fields (can be None)
    location: str | None = Field(default=None, max_length=100)
    applied_date: date | None = None
    source: str | None = Field(default=None, max_length=100)
    notes: str | None = Field(default=None, max_length=500)

    # Default value if not provided
    favorite: bool = False


# Schema used when creating a new application
class JobApplicationCreate(JobApplicationBase):
    pass


# Schema used when updating an application
class JobApplicationUpdate(JobApplicationBase):
    pass


# Schema used for API responses (includes ID)
class JobApplicationResponse(JobApplicationBase):
    id: int