from langchain_core.tools import tool

from app.clients.vet_api import VetAPIClient
from app.schemas.visit import CreateVisitRequest, UpdateVisitRequest

client = VetAPIClient()

@tool
async def create_visit(
    pet_id: int,
    visit_date: str,
    reason: str,
    diagnosis: str,
    treatment: str,
):
    """
    Create a visit for a pet.
    """
    payload = {
        "visit_date": visit_date,
        "reason": reason,
        "diagnosis": diagnosis,
        "treatment": treatment,
    }
    return await client.post(
        f"/pets/{pet_id}/visits",
        payload,
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
    visit_date: str | None = None,
    reason: str | None = None,
    diagnosis: str | None = None,
    treatment: str | None = None,
):
    """
    Update a visit.
    """
    payload = {
        "visit_date": visit_date,
        "reason": reason,
        "diagnosis": diagnosis,
        "treatment": treatment,
    }
    
    payload =  {k: v for k, v in payload.items() if v is not None}
    return await client.put(
        f"/visits/{visit_id}",
        payload,
    )

@tool
async def delete_visit(visit_id: int):
    """
    Delete a visit.
    """
    return await client.delete(
        f"/visits/{visit_id}"
    )