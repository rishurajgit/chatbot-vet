# from langchain_core.tools import tool

# from app.clients.vet_api import VetAPIClient
# # from app.schemas.owner import CreateOwnerRequest

# client = VetAPIClient()

# @tool
# async def create_owner(
#     name: str,
#     phone: str,
#     email: str,
# ):
#     """
#     Create a new owner.
#     """
    
#     payload = {
#         "name": name,
#         "phone": phone,
#         "email": email,
#     }
#     return await client.post(
#         "/Owners",
#         payload,
#     )


# @tool
# async def get_owner_pets(owner_id: int):
#     """
#     Retrieve all pets belonging to an owner.
#     """
#     return await client.get(
#         f"/Owners/{owner_id}/pets"
#     )

from langchain_core.tools import tool

from app.clients.vet_api import vet_api


@tool
async def get_all_owners(
    search: str | None = None,
    page: int = 1,
    limit: int = 10,
):
    """
    Get all owners.

    This tool can also search owners by name using the search parameter.
    """

    params = {
        "search": search,
        "page": page,
        "limit": limit,
    }

    params = {k: v for k, v in params.items() if v is not None}

    return await vet_api.request(
        method="GET",
        endpoint="/Owners",
        params=params,
    )


@tool
async def get_owner(owner_id: int):
    """
    Retrieve a single owner using the owner's ID.
    """

    return await vet_api.request(
        method="GET",
        endpoint=f"/Owners/{owner_id}",
    )


@tool
async def create_owner(
    name: str,
    phone: str,
    email: str,
):
    """
    Create a new owner.

    Call this tool only when all required information is available:
    - name
    - phone
    - email
    """

    return await vet_api.request(
        method="POST",
        endpoint="/Owners",
        json={
            "name": name,
            "phone": phone,
            "email": email,
        },
    )


@tool
async def update_owner(
    owner_id: int,
    name: str | None = None,
    phone: str | None = None,
    email: str | None = None,
):
    """
    Update an existing owner.

    Provide only the fields that need to be updated.
    """

    payload = {
        "name": name,
        "phone": phone,
        "email": email,
    }

    payload = {k: v for k, v in payload.items() if v is not None}

    return await vet_api.request(
        method="PUT",
        endpoint=f"/Owners/{owner_id}",
        json=payload,
    )


@tool
async def delete_owner(owner_id: int):
    """
    Delete an owner using the owner's ID.
    """

    return await vet_api.request(
        method="DELETE",
        endpoint=f"/Owners/{owner_id}",
    )


@tool
async def get_owner_pets(owner_id: int):
    """
    Retrieve all pets belonging to a specific owner.
    """

    return await vet_api.request(
        method="GET",
        endpoint=f"/Owners/{owner_id}/pets",
    )