from langchain_core.tools import tool

from app.clients.vet_api import VetAPIClient
from app.schemas.visit import CreateVisitRequest, UpdateVisitRequest

client = VetAPIClient()

@tool
async def create_visit(
    pet_id: int,
    data: CreateVisitRequest,
):
    """
    Create a visit for a pet.
    """
    return await client.post(
        f"/pets/{pet_id}/visits",
        data.model_dump()
    )
    
@tool
async def get_pet_visits(pet_id: int):
    """
    Retrieve all visits for a pet.
    Use this tool when the user asks to:
    - show visits
    - list visits
    - display a pet's medical history
    """
    return await client.get(
        f"/pets/{pet_id}/visits"
    )
    
@tool
async def update_visit(
    visit_id: int,
    data: UpdateVisitRequest,
):
    """
    Update a visit.
    """
    return await client.put(
        f"/visits/{visit_id}",
        data.model_dump(exclude_none=True)
    )

@tool
async def delete_visit(visit_id: int):
    """
    Delete a visit.
    """
    return await client.delete(
        f"/visits/{visit_id}"
    )