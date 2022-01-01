import requests
from page_loader.logger import get_logger


logger = get_logger(__name__)


def make_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as err:
        logger.error('Network error!')
        raise requests.exceptions.RequestException(err)


def download_resource_item(url):
    try:
        response = make_request(url)
    except requests.HTTPError as err:
        logger.warning(str(err))
    return response.content
