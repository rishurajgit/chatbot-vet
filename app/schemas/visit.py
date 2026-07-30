from pydantic import BaseModel


class CreateVisitRequest(BaseModel):
    visit_date: str
    reason: str
    diagnosis: str
    treatment: str


class UpdateVisitRequest(BaseModel):
    visit_date: str | None = None
    reason: str | None = None
    diagnosis: str | None = None
    treatment: str | None = None