from bs4 import BeautifulSoup
import os
from page_loader import url_tools

ATTRIBUTES = {
    'img': 'src',
    'link': 'href',
    'script': 'src'
}


def process_html(page, url):
    soup = BeautifulSoup(page.text, 'html.parser')
    resources = soup.find_all(ATTRIBUTES.keys())
    resources_dir = url_tools.to_dir_name(url, '_files')
    resources_urls = []
    for resource in resources:
        raw_resource_url = list(map(resource.get, ATTRIBUTES.values()))
        resource_url = next(
            (item for item in raw_resource_url if item is not None), None
        )
        if not resource_url:
            continue
        resource_url_tag = ATTRIBUTES[resource.name]
        resource_url = url_tools.join(
            resource[resource_url_tag], url
        )
        if url_tools.get_netloc(resource_url) == url_tools.get_netloc(url):
            resources_urls.append(resource_url)
            resource_file_name = url_tools.to_file_name(resource_url)
            resource[resource_url_tag] = os.path.join(
                resources_dir, resource_file_name
            )
    return soup.prettify(), resources_urls
