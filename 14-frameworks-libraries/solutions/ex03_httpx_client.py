import httpx


class ApiError(Exception):
    def __init__(self, message: str, status_code: int) -> None:
        super().__init__(message)
        self.status_code = status_code


def get_json(client: httpx.Client, url: str) -> dict[str, object]:
    response = client.get(url)
    try:
        response.raise_for_status()
    except httpx.HTTPStatusError as exc:
        raise ApiError(f"GET {url} failed with {response.status_code}", response.status_code) from exc
    return response.json()


def fetch_with_retry(client: httpx.Client, url: str, attempts: int = 3) -> dict[str, object]:
    last_status = 0
    for _ in range(attempts):
        response = client.get(url)
        if response.status_code < 400:
            return response.json()
        last_status = response.status_code
        if response.status_code < 500:
            raise ApiError(f"GET {url} failed with {response.status_code}", response.status_code)
    raise ApiError(f"GET {url} failed after {attempts} attempts", last_status)
