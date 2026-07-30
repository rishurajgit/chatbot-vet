from langchain_core.tools import tool

from app.clients.vet_api import VetAPIClient
# from app.schemas.owner import CreateOwnerRequest

client = VetAPIClient()

@tool
async def create_owner(
    name: str,
    phone: str,
    email: str,
):
    """
    Create a new owner.
    """
    
    payload = {
        "name": name,
        "phone": phone,
        "email": email,
    }
    return await client.post(
        "/Owners",
        payload,
    )


@tool
async def get_owner_pets(owner_id: int):
    """
    Retrieve all pets belonging to an owner.
    """
    return await client.get(
        f"/Owners/{owner_id}/pets"
    )