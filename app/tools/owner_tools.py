from langchain_core.tools import tool

from app.clients.vet_api import VetAPIClient
from app.schemas.owner import CreateOwnerRequest

client = VetAPIClient()

@tool
async def create_owner(data: CreateOwnerRequest):
    """
    Create a new owner.
    """
    return await client.post(
        "/owners",
        data.model_dump()
    )


@tool
async def get_owner_pets(owner_id: int):
    """
    Retrieve all pets belonging to an owner.
    """
    return await client.get(
        f"/Owners/{owner_id}/pets"
    )