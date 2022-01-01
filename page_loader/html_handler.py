import os
from bs4 import BeautifulSoup
from page_loader import url_tools
from page_loader.logger import get_logger

ATTRIBUTES = {
    'img': 'src',
    'link': 'href',
    'script': 'src'
}

logger = get_logger(__name__)


def process_html(page, url):
    soup = BeautifulSoup(page.text, 'html.parser')
    resources = soup.find_all(ATTRIBUTES.keys())
    resources_dir = url_tools.to_dir_name(url, '_files')
    resources_urls = []
    for resource in resources:
        resource_url_tag = ATTRIBUTES[resource.name]
        resource_url = resource.get(resource_url_tag)
        if not resource_url:
            continue
        resource_url = url_tools.join(url, resource[resource_url_tag])
        if url_tools.get_netloc(resource_url) == url_tools.get_netloc(url):
            resources_urls.append(resource_url)
            resource_file_name = url_tools.to_file_name(resource_url)
            resource[resource_url_tag] = os.path.join(
                resources_dir, resource_file_name
            )
    return soup.prettify(), resources_urls