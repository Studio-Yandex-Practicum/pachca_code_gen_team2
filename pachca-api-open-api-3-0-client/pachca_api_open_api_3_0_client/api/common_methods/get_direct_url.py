from http import HTTPStatus
from typing import Any, Optional

import httpx

from ... import errors
from ...models.direct_response import DirectResponse
from ...types import Response


def _get_kwargs_getDirectUrl(
    self,
    body: DirectResponse,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/direct_url",
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response_getDirectUrl(self, response: httpx.Response) -> Optional[Any]:
    if response.status_code == 204:
        return None
    if self.client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response_getDirectUrl(self, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=self._parse_response_getDirectUrl(response=response),
    )
