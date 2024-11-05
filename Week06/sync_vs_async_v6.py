import requests
import logging
import time

logging.basicConfig(
    format="%(levelname)s @ %(asctime)s : %(message)s",
    datefmt="%d.%m.%Y %H:%M:%S",
    level=logging.DEBUG,
    handlers=[logging.FileHandler("requests.log", mode="w"), logging.StreamHandler()],
)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/106.0.0.0 Safari/537.36"
}
BASE_URL = "https://www.canbula.com/prime"
MAX_RETRIES = 3
TIMEOUT = 10


def sync_request(session: requests.Session, n: int) -> dict:
    """Synchronous request with error handling, logging, and retry logic"""
    for attempt in range(MAX_RETRIES):
        try:
            response = session.get(f"{BASE_URL}/{n}", headers=HEADERS, timeout=TIMEOUT)
            response.raise_for_status()
            logging.debug(f"Request returned with status code {response.status_code}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Request for {n} failed: {e} (attempt {attempt + 1})")
            time.sleep(2**attempt)  # Exponential backoff
    logging.error(f"Request for {n} failed after {MAX_RETRIES} attempts")
    return {}


if __name__ == "__main__":
    with requests.Session() as session:
        print(sync_request(session, 5))
