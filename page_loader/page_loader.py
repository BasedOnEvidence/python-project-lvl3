import os
from progress.bar import ChargingBar
from page_loader.logger import get_logger
from page_loader.html_parser import parse_html

from page_loader.network_tools import (
    download_resource_item,
    make_request
)
from page_loader.url_tools import (
    convert_url_to_file_name,
)
from page_loader.os_tools import (
    save_file,
    create_directory
)


logger = get_logger(__name__)


def download(url, output_path):
    file_name = convert_url_to_file_name(url, '.html')
    folder_name = file_name.replace('.html', '_files')
    file_path = os.path.join(output_path, file_name)
    resources_path = os.path.join(output_path, folder_name)
    response = make_request(url)
    html, resources = parse_html(response, url, resources_path)
    save_file(file_path, html, mode='w')
    logger.info(resources)
    if not os.path.exists(resources_path) and resources:
        logger.info('Creating {}'.format(resources_path))
        create_directory(resources_path)
    bar = ChargingBar('Downloading resources:', max=len(resources))
    for res_url, res_path in resources.items():
        file_obj = download_resource_item(res_url)
        save_file(res_path, file_obj)
        bar.next()
    bar.finish()
    return file_path
