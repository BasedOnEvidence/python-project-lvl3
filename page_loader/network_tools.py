import requests
from page_loader.logger import get_logger


logger = get_logger(__name__)


def get_page_obj(url):
    response = requests.get(url)
    response.raise_for_status()
    return response


def download_resource_item(url):
    try:
        response = requests.get(url)
    except requests.HTTPError as err:
        logger.error(str(err), exc_info=True)
    logger.debug('{} is downloaded'.format(url))
    return response.content
