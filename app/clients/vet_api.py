import httpx

from app.core.config import settings


class VetAPIClient:
    def __init__(self):
        self.client = httpx.AsyncClient(
            base_url=settings.VET_API_BASE_URL,
            timeout=30.0,
        )

    async def get(self, endpoint, headers=None, params=None):
        response = await self.client.get(
            endpoint,
            headers=headers,
            params=params,
        )
        response.raise_for_status()
        return response.json()

    async def post(self, endpoint, data, headers=None):
        response = await self.client.post(
            endpoint,
            json=data,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    async def put(self, endpoint, data, headers=None):
        response = await self.client.put(
            endpoint,
            json=data,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()

    async def delete(self, endpoint, headers=None):
        response = await self.client.delete(
            endpoint,
            headers=headers,
        )
        response.raise_for_status()

        if response.content:
            return response.json()

        return {"success": True}

    async def close(self):
        await self.client.aclose()