import requests
import logging

logging.basicConfig(
    format="%(levelname)s @ %(asctime)s : %(message)s",
    datefmt="%d.%m.%Y %H:%M:%S",
    level=logging.DEBUG,
    handlers=[logging.FileHandler("requests.log", mode="w"), logging.StreamHandler()],
)
BASE_URL = "https://www.canbula.com/prime"


def sync_request(n: int) -> dict:
    """Synchronous request with error handling and logging"""
    try:
        response = requests.get(f"{BASE_URL}/{n}")
        response.raise_for_status()
        logging.debug(f"Request returned with status code {response.status_code}")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Request for {n} failed: {e}")
        return {}


if __name__ == "__main__":
    logging.critical("A critical error occurred")
    logging.debug("A debug message")
    logging.error("An error occurred")
    logging.info("An info message")
    logging.warning("A warning message")
    result = sync_request(5)
    print(result)
