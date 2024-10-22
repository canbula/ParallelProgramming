import requests

BASE_URL = "https://www.canbula.com/prime"


def sync_request(n: int) -> dict:
    """Synchronous request with error handling"""
    try:
        response = requests.get(f"{BASE_URL}/{n}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return {}


if __name__ == "__main__":
    result = sync_request(5)
    print(result)
