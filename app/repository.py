# Import schemas for data validation and structure
from app.schemas import JobApplicationCreate, JobApplicationResponse, JobApplicationUpdate


# Repository class responsible for managing job applications (in-memory storage)
class ApplicationRepository:
    def __init__(self) -> None:
        # Dictionary to store applications (key = id, value = application object)
        self._applications: dict[int, JobApplicationResponse] = {}

        # Auto-increment ID counter
        self._next_id = 1


    # Return all stored applications
    def list_all(self) -> list[JobApplicationResponse]:
        return list(self._applications.values())


    # Retrieve a single application by its ID
    def get_by_id(self, application_id: int) -> JobApplicationResponse | None:
        return self._applications.get(application_id)


    # Create a new application
    def create(self, data: JobApplicationCreate) -> JobApplicationResponse:
        # Build response object with generated ID + input data
        application = JobApplicationResponse(
            id=self._next_id,
            **data.model_dump()  # Convert Pydantic model to dict
        )

        # Store application in memory
        self._applications[self._next_id] = application

        # Increment ID for next application
        self._next_id += 1

        return application


    # Update an existing application
    def update(
        self,
        application_id: int,
        data: JobApplicationUpdate
    ) -> JobApplicationResponse | None:

        # Return None if application does not exist
        if application_id not in self._applications:
            return None

        # Create updated object with same ID and new data
        updated_application = JobApplicationResponse(
            id=application_id,
            **data.model_dump()
        )

        # Replace existing application
        self._applications[application_id] = updated_application

        return updated_application


    # Delete an application by ID
    def delete(self, application_id: int) -> bool:

        # Return False if application does not exist
        if application_id not in self._applications:
            return False

        # Remove application from storage
        del self._applications[application_id]

        return True