from app.schemas import JobApplicationCreate, JobApplicationResponse, JobApplicationUpdate


class ApplicationRepository:
    def __init__(self) -> None:
        self._applications: dict[int, JobApplicationResponse] = {}
        self._next_id = 1

    def list_all(self) -> list[JobApplicationResponse]:
        return list(self._applications.values())

    def get_by_id(self, application_id: int) -> JobApplicationResponse | None:
        return self._applications.get(application_id)

    def create(self, data: JobApplicationCreate) -> JobApplicationResponse:
        application = JobApplicationResponse(
            id=self._next_id,
            **data.model_dump()
        )
        self._applications[self._next_id] = application
        self._next_id += 1
        return application

    def update(
        self,
        application_id: int,
        data: JobApplicationUpdate
    ) -> JobApplicationResponse | None:
        if application_id not in self._applications:
            return None

        updated_application = JobApplicationResponse(
            id=application_id,
            **data.model_dump()
        )
        self._applications[application_id] = updated_application
        return updated_application

    def delete(self, application_id: int) -> bool:
        if application_id not in self._applications:
            return False

        del self._applications[application_id]
        return True