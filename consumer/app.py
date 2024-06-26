import requests
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger(__name__)


def query_backend():
    url = "http://backend:8000/fetch"
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                log.info("Successfully fetched data: %s", response.json())
            else:
                log.error("Failed to fetch data, status code: %s", response.status_code)
        except requests.exceptions.RequestException as e:
            log.error("Error querying backend: %s", e)


if __name__ == "__main__":
    query_backend()