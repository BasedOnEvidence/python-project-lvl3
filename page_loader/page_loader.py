import os
from page_loader.network_tools import (
    download_resource_item,
    get_page_obj
)
from page_loader.url_tools import (
    convert_url_to_file_name,
    convert_url_to_standart_view,
    is_url_in_domain
)
from page_loader.os_tools import (
    save_file,
    create_directory
)
from progress.bar import ChargingBar
from page_loader.logger import get_logger


logger = get_logger(__name__)

RESOURCES = {
    'img': 'src',
    'link': 'href',
    'script': 'src'
}


def download(url, output_path):
    soup = get_page_obj(url)
    file_name = convert_url_to_file_name(url)
    file_path = os.path.join(output_path, file_name + '.html')
    resources_path = os.path.join(output_path, file_name + '_files')
    logger.info('File path: {}'.format(file_path))
    logger.info('Resources path: {}'.format(resources_path))
    resources = soup.find_all(RESOURCES.keys())
    if not os.path.exists(resources_path) and resources:
        create_directory(resources_path)
    bar = ChargingBar('Downloading resources:', max=len(resources))
    for resource in resources:
        raw_resource_url = list(map(resource.get, RESOURCES.values()))
        resource_url = next(
            (item for item in raw_resource_url if item is not None), None
        )
        bar.next()
        if not resource_url:
            continue
        resource_url_tag = RESOURCES[resource.name]
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
