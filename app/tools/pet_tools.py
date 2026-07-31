# from langchain_core.tools import tool

# from app.clients.vet_api import VetAPIClient

# from app.schemas.pet import CreatePetRequest, UpdatePetRequest

# client = VetAPIClient()


# @tool
# async def get_all_pets():
#     """
#     Retrieve all pets from the veterinary system.
#     """
#     return await client.get("/pets")


# @tool
# async def get_pet(pet_id: int):
#     """
#     Retrieve a pet by its ID.
#     """
#     return await client.get(f"/pets/{pet_id}")


# @tool
# async def delete_pet(pet_id: int):
#     """
#     Delete a pet by its ID.
#     """
#     return await client.delete(f"/pets/{pet_id}")

# @tool
# async def create_pet(
#     petname: str,
#     species: str,
#     breed: str,
#     age: int,
#     owner_id: int,
# ):
#     """
#     Create a new pet.

#     Args:
#         data: Pet information.
#     """
#     payload = {
#         "petname": petname,
#         "species": species,
#         "breed": breed,
#         "age": age,
#         "owner_id": owner_id,
#     }
#     return await client.post(
#         "/pets",
#         payload
#         )

# @tool
# async def update_pet(
#     pet_id: int,
#     name: str | None = None,
#     species: str | None = None,
#     breed: str | None = None,
#     age: int | None = None,
#     owner_id: int | None = None,
# ):
#     """
#     Update an existing pet.
#     """
#     payload = {
#         "name": name,
#         "species": species,
#         "breed": breed,
#         "age": age,
#         "owner_id": owner_id,
#     }
#     payload = {
#         key: value
#         for key, value in payload.items()
#         if value is not None
#     }
#     return await client.put(
#         f"/pets/{pet_id}",
#         payload
#     )
    
# @tool
# async def search_pets(search: str):
#     """
#     Search pets by name or keyword.
#     Use this tool whenever the user refers to a pet by name instead of ID.
#     """
    
#     return await client.get(
#         "/pets",
#         params={"search": search}
#     )

from langchain_core.tools import tool

from app.clients.vet_api import vet_api


@tool
async def get_all_pets(
    species: str | None = None,
    breed: str | None = None,
    min_age: int | None = None,
    max_age: int | None = None,
    owner_id: int | None = None,
    search: str | None = None,
    page: int = 1,
    limit: int = 10,
    sort_by: str | None = None,
    sort_order: str = "asc",
):
    """
    Get all pets.

    This tool can also search and filter pets using:
    - species
    - breed
    - age range
    - owner_id
    - pet name search
    """

    params = {
        "species": species,
        "breed": breed,
        "min_age": min_age,
        "max_age": max_age,
        "owner_id": owner_id,
        "search": search,
        "page": page,
        "limit": limit,
        "sort_by": sort_by,
        "sort_order": sort_order,
    }

    params = {k: v for k, v in params.items() if v is not None}

    return await vet_api.request(
        method="GET",
        endpoint="/pets",
        params=params,
    )


@tool
async def get_pet(pet_id: int):
    """
    Retrieve a pet using its ID.
    """

    return await vet_api.request(
        method="GET",
        endpoint=f"/pets/{pet_id}",
    )


@tool
async def create_pet(
    petname: str,
    species: str,
    breed: str,
    age: int,
    owner_id: int,
):
    """
    Create a new pet.

    Call this tool only after all required information is available:
    - petname
    - species
    - breed
    - age
    - owner_id
    """

    return await vet_api.request(
        method="POST",
        endpoint="/pets",
        json={
            "petname": petname,
            "species": species,
            "breed": breed,
            "age": age,
            "owner_id": owner_id,
        },
    )


@tool
async def update_pet(
    pet_id: int,
    petname: str,
    species: str,
    breed: str,
    age: int,
    owner_id: int,
):
    """
    Update an existing pet.

    Use this tool only when the pet ID is known.
    """

    return await vet_api.request(
        method="PUT",
        endpoint=f"/pets/{pet_id}",
        json={
            "petname": petname,
            "species": species,
            "breed": breed,
            "age": age,
            "owner_id": owner_id,
        },
    )


@tool
async def delete_pet(pet_id: int):
    """
    Delete a pet using its ID.
    """

    return await vet_api.request(
        method="DELETE",
        endpoint=f"/pets/{pet_id}",
    )
    