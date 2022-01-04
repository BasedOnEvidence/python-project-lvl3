import os
from bs4 import BeautifulSoup
from page_loader import name_assigner
from urllib.parse import urljoin, urlparse

ATTRIBUTES = {
    'img': 'src',
    'link': 'href',
    'script': 'src'
}


def process_html(page, url):
    soup = BeautifulSoup(page.text, 'html.parser')
    resources = soup.find_all(ATTRIBUTES.keys())
    resources_dir = name_assigner.to_dir_name(url, '_files')
    resources_urls = []
    for resource in resources:
        resource_url_tag = ATTRIBUTES[resource.name]
        resource_url = resource.get(resource_url_tag)
        if not resource_url:
            continue
        resource_url = urljoin(url, resource[resource_url_tag])
        url_netloc = urlparse(url).netloc
        if urlparse(resource_url).netloc == url_netloc:
            resources_urls.append(resource_url)
            resource_file_name = name_assigner.to_file_name(resource_url)
            resource[resource_url_tag] = os.path.join(
                resources_dir, resource_file_name
            )
    return soup.prettify(), resources_urls
