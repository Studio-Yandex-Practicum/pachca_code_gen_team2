from typing import Any

import httpx


class HttpClient:
    @staticmethod
    async def send_request(method: str, url: str, token: str, **kwargs: Any) -> httpx.Response:
        headers = kwargs.get('headers', {})
        headers['Authorization'] = f"Bearer {token}"
        kwargs['headers'] = headers

        async with httpx.AsyncClient() as client:
            response = await client.request(method, url, **kwargs)
        return response
