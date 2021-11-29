import requests
import os
from bs4 import BeautifulSoup
from page_loader.tools import (
    get_resources_path,
    get_file_name_from_url,
    get_domain_from_url,
    is_url_in_domain,
    convert_url_to_html_path,
    make_url_absolute
)
from page_loader.logger import get_logger
from progress.bar import ChargingBar


logger = get_logger(__name__)

RESOURCES = {
    'img': 'src',
    'link': 'href',
    'script': 'src'
}


def get_resources(txt_data):
    soup = BeautifulSoup(txt_data, 'html.parser')
    data = {}
    for tag in RESOURCES.keys():
        tags = soup.find_all(tag, {RESOURCES[tag]: True})
        urls = [item[RESOURCES[tag]] for item in tags]
        data[tag] = urls
    return data


def download_resources(txt_data, output_path, content_path, base_url):
    logger.info('Current base url: {}'.format(base_url))
    current_txt = txt_data
    domain = get_domain_from_url(base_url)
    urls = get_resources(txt_data)
    logger.info('Urls: {}'.format(urls))
    bar_max_length = sum([len(item) for item in urls.values()])
    logger.info('Items count: {}'.format(bar_max_length))
    bar = ChargingBar('Downloading resources:', max=bar_max_length)
    for tag in RESOURCES.keys():
        for url in urls[tag]:
            if is_url_in_domain(domain, url):
                file_name = get_file_name_from_url(url)
                resource_path = os.path.join(content_path, file_name)
                current_txt = current_txt.replace(url, resource_path)
                with open(resource_path, 'wb') as f:
                    url = make_url_absolute(base_url, url)
                    logger.info('Current content url: {}'.format(url))
                    response = requests.get(url)
                    f.write(response.content)
            bar.next()
    with open(output_path, 'w') as file_:
        file_.write(current_txt)
    bar.finish()


def download(url, output_path):
    response = requests.get(url, allow_redirects=True)
    if response.status_code >= 400:
        raise Exception('Status code = {}'.format(response.status_code))
    txt_data = response.text
    file_path = convert_url_to_html_path(url, output_path)
    resources_path = get_resources_path(file_path)
    os.mkdir(resources_path)
    logger.info('File path: {}'.format(file_path))
    logger.info('Resources path: {}'.format(resources_path))
    download_resources(txt_data, file_path, resources_path, url)
    return file_path
