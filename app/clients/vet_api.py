# import httpx

# from app.core.config import settings


# class VetAPIClient:
#     def __init__(self):
#         self.client = httpx.AsyncClient(
#             base_url=settings.VET_API_BASE_URL,
#             timeout=30.0,
#             headers={
#                 "Authorization": f"Bearer {settings.VET_API_TOKEN}"
#             },
#         )

#     async def get(self, endpoint, headers=None, params=None):
#         response = await self.client.get(
#             endpoint,
#             headers=headers,
#             params=params,
#         )
#         response.raise_for_status()
#         return response.json()

#     async def post(self, endpoint, data, headers=None):
#         response = await self.client.post(
#             endpoint,
#             json=data,
#             headers=headers,
#         )
#         response.raise_for_status()
#         return response.json()

#     async def put(self, endpoint, data, headers=None):
#         response = await self.client.put(
#             endpoint,
#             json=data,
#             headers=headers,
#         )
#         response.raise_for_status()
#         return response.json()

#     async def delete(self, endpoint, headers=None):
#         response = await self.client.delete(
#             endpoint,
#             headers=headers,
#         )
#         response.raise_for_status()

#         if response.content:
#             return response.json()

#         return {"success": True}

#     async def close(self):
#         await self.client.aclose()

import httpx

from app.core.config import settings


class VetAPIClient:
    def __init__(self):
        self.base_url = settings.VET_API_BASE_URL
        self.token = settings.VET_API_TOKEN

    async def request(
        self,
        method: str,
        endpoint: str,
        params: dict | None = None,
        json: dict | None = None,
    ):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

        async with httpx.AsyncClient(
            base_url=self.base_url,
            headers=headers,
            timeout=30,
        ) as client:

            response = await client.request(
                method=method,
                url=endpoint,
                params=params,
                json=json,
                headers=headers,
            )

            response.raise_for_status()
            
            if response.content:
                return response.json()

            return {"success": True}


vet_api = VetAPIClient()