import requests
from page_loader.os_tools import save_file
from page_loader.logger import get_logger


logger = get_logger(__name__)


def get_page_obj(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as err:
        logger.error(err)
        raise requests.exceptions.RequestException


def download_resource_item(url, path):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        logger.error(err)
        raise requests.exceptions.RequestException
    logger.debug('{} is downloaded'.format(url))
    file_obj = response.content
    save_file(path, file_obj)
