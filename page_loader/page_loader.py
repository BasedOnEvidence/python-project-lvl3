import requests
import os
from bs4 import BeautifulSoup
from page_loader.tools import (
    get_resources_path,
    get_domain_from_url,
    is_url_in_domain,
    make_url_absolute
)
from page_loader.url_tools import (
    convert_url_to_file_name
)
from page_loader.logger import get_logger
from progress.bar import ChargingBar


logger = get_logger(__name__)

RESOURCES = {
    'img': 'src',
    'link': 'href',
    'script': 'src'
}


def get_url(resource, base_url):
    url = ''
    if RESOURCES[resource.name] in resource.attrs:
        url = resource[RESOURCES[resource.name]]
    return make_url_absolute(base_url, url)


def download_resources(resources, content_path, base_url):
    logger.info('Current base url: {}'.format(base_url))
    domain = get_domain_from_url(base_url)
    logger.info('Tags: {}'.format(resources))
    bar_max_length = len(resources)
    logger.info('Items count: {}'.format(bar_max_length))
    bar = ChargingBar('Downloading resources:', max=bar_max_length)
    for resource in resources:
        url = get_url(resource, base_url)
        logger.info('Current resource url: {}'.format(url))
        if is_url_in_domain(domain, url):
            cutted_url, ext = os.path.splitext(url)
            file_name = convert_url_to_file_name(cutted_url) + ext
            logger.info('Current resource file name: {}'.format(file_name))
            resource_path = os.path.join(content_path, file_name)
            logger.info('Current resource path: {}'.format(resource_path))
            with open(resource_path, 'wb') as f:
                logger.info('Current content url: {}'.format(url))
                response = requests.get(url)
                f.write(response.content)
            resource_path = os.path.join(
                os.path.split(content_path)[-1], file_name
            )
            resource[RESOURCES[resource.name]] = resource_path
        bar.next()
    bar.finish()


def download(url, output_path):
    response = requests.get(url, allow_redirects=True)
    if response.status_code >= 400:
        raise Exception('Status code = {}'.format(response.status_code))
    file_name = convert_url_to_file_name(url) + '.html'
    file_path = os.path.join(output_path, file_name)
    resources_path = get_resources_path(file_path)
    os.mkdir(resources_path)
    logger.info('File path: {}'.format(file_path))
    logger.info('Resources path: {}'.format(resources_path))
    soup = BeautifulSoup(response.text, 'html.parser')
    resources = soup.find_all(RESOURCES.keys())
    download_resources(resources, resources_path, url)
    with open(file_path, 'w') as f:
        f.write(soup.prettify(formatter="html5"))
    return file_path
