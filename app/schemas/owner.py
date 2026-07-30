from pydantic import BaseModel


class CreateOwnerRequest(BaseModel):
    name: str
    email: str
    phone: str