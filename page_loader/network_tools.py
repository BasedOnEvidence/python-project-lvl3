import requests
import logging


def make_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as err:
        logging.error('Network error!')
        raise requests.exceptions.RequestException(err)


def download_resource_item(url):
    try:
        response = make_request(url)
    except requests.HTTPError as err:
        logging.warning(str(err))
    return response.content
