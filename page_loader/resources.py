import os
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup
from page_loader import url_formatter

TAG_ATTRIBUTES = {
    'img': 'src',
    'link': 'href',
    'script': 'src'
}


def process_html(html, url):
    soup = BeautifulSoup(html, 'html.parser')
    resources = soup.find_all(TAG_ATTRIBUTES.keys())
    resources_dir = url_formatter.to_dir_name(url, '_files')
    resources_urls = []
    for resource in resources:
        resource_url_tag = TAG_ATTRIBUTES[resource.name]
        resource_url = resource.get(resource_url_tag)
        if not resource_url:
            continue
        resource_url = urljoin(url, resource[resource_url_tag])
        url_netloc = urlparse(url).netloc
        if urlparse(resource_url).netloc == url_netloc:
            resources_urls.append(resource_url)
            resource_file_name = url_formatter.to_file_name(resource_url)
            resource[resource_url_tag] = os.path.join(
                resources_dir, resource_file_name
            )
    return soup.prettify(), resources_urls
