import os
from progress.bar import ChargingBar
from page_loader.logger import get_logger

from page_loader.network_tools import (
    download_resource_item,
    get_page_obj
)
from page_loader.url_tools import (
    convert_url_to_file_name,
    convert_url_to_standart_view,
    is_url_in_domain,
    get_resource_url
)
from page_loader.os_tools import (
    save_file,
    create_directory
)
from page_loader.constants import ATTRIBUTES


logger = get_logger(__name__)


def download(url, output_path):
    file_name = convert_url_to_file_name(url)
    file_path = os.path.join(output_path, file_name + '.html')
    resources_path = os.path.join(output_path, file_name + '_files')
    soup = get_page_obj(url)
    resources = soup.find_all(ATTRIBUTES.keys())
    if not os.path.exists(resources_path) and resources:
        create_directory(resources_path)
    bar = ChargingBar('Downloading resources:', max=len(resources))
    for resource in resources:
        resource_url = get_resource_url(resource)
        bar.next()
        if not resource_url:
            continue
        resource_url_tag = ATTRIBUTES[resource.name]
        resource_url = convert_url_to_standart_view(
            resource[resource_url_tag], url
        )
        cutted_url, ext = os.path.splitext(resource_url)
        if ext == '':
            ext = '.html'
        resource_file_name = convert_url_to_file_name(cutted_url) + ext
        if is_url_in_domain(resource_url, url):
            resource_file_path = os.path.join(
                resources_path, resource_file_name
            )
            download_resource_item(resource_url, resource_file_path)
            resource[resource_url_tag] = os.path.join(
                file_name + '_files', resource_file_name
            )
    bar.finish()
    save_file(file_path, soup, 'w')
    return file_path
