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
    
    
    