from pydantic import BaseModel


class CreatePetRequest(BaseModel):
    name: str
    species: str
    breed: str
    age: int
    owner_id: int
    
class UpdatePetRequest(BaseModel):
    name: str | None = None
    species: str | None = None
    breed: str | None = None
    age: int | None = None
    owner_id: int | None = None