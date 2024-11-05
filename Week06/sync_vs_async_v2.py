import requests

BASE_URL = "https://www.canbula.com/prime"


def sync_request(n: int) -> dict:
    """Basic synchronous request"""
    response = requests.get(f"{BASE_URL}/{n}")
    return response.json()


if __name__ == "__main__":
    result = sync_request(5)
    print(result)
