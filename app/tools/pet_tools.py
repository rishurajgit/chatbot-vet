from langchain_core.tools import tool

from app.clients.vet_api import VetAPIClient

from app.schemas.pet import CreatePetRequest, UpdatePetRequest

client = VetAPIClient()


@tool
async def get_all_pets():
    """
    Retrieve all pets from the veterinary system.
    """
    return await client.get("/pets")


@tool
async def get_pet(pet_id: int):
    """
    Retrieve a pet by its ID.
    """
    return await client.get(f"/pets/{pet_id}")


@tool
async def delete_pet(pet_id: int):
    """
    Delete a pet by its ID.
    """
    return await client.delete(f"/pets/{pet_id}")

@tool
async def create_pet(data: CreatePetRequest):
    """
    Create a new pet.

    Args:
        data: Pet information.
    """
    return await client.post(
        "/pets",
        data.model_dump ()
        )

@tool
async def update_pet(
    pet_id: int,
    data: UpdatePetRequest,
):
    """
    Update an existing pet.
    """
    return await client.put(
        f"/pets/{pet_id}",
        data.model_dump(exclude_none=True)
    )