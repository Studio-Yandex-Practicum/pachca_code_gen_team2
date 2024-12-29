import httpx
from typing import Any, Dict

class HttpClient:
    @staticmethod
    async def request(method: str, url: str, **kwargs: Any) -> httpx.Response:
        async with httpx.AsyncClient() as client:
            response = await client.request(method, url, **kwargs)
            return response
