import requests

BASE_URL = "https://www.canbula.com/prime"


def sync_request(n: int):
    """Basic synchronous request"""
    requests.get(f"{BASE_URL}/{n}")
    print(f"Sync request {n} done")


if __name__ == "__main__":
    sync_request(5)
