from bs4 import BeautifulSoup
import os
from page_loader.constants import ATTRIBUTES
from page_loader.url_tools import (
    convert_url_to_file_name,
    convert_url_to_standart_view,
    is_url_in_domain
)


def parse_html_page(page, url, resources_path):
    soup = BeautifulSoup(page.text, 'html.parser')
    resources = soup.find_all(ATTRIBUTES.keys())
    data_for_download = {}
    for resource in resources:
        raw_resource_url = list(map(resource.get, ATTRIBUTES.values()))
        resource_url = next(
            (item for item in raw_resource_url if item is not None), None
        )
        if not resource_url:
            continue
        resource_url_tag = ATTRIBUTES[resource.name]
        resource_url = convert_url_to_standart_view(
            resource[resource_url_tag], url
        )
        cutted_url, ext = os.path.splitext(resource_url)
        resource_file_name = convert_url_to_file_name(cutted_url, ext)
        if is_url_in_domain(resource_url, url):
            resource_file_path = os.path.join(
                resources_path, resource_file_name
            )
            data_for_download[resource_url] = resource_file_path
            resource[resource_url_tag] = os.path.join(
                os.path.basename(resources_path), resource_file_name
            )
    return soup, data_for_download
