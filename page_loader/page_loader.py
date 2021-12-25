import os
from progress.bar import ChargingBar
from page_loader.logger import get_logger
from page_loader.bs_parser import parse_html_page

from page_loader.network_tools import (
    download_resource_item,
    get_page_obj
)
from page_loader.url_tools import (
    convert_url_to_file_name,
)
from page_loader.os_tools import (
    save_file,
    save_bs_object,
    create_directory
)


logger = get_logger(__name__)


def download(url, output_path):
    file_name = convert_url_to_file_name(url, '.html')
    folder_name = file_name.replace('.html', '_files')
    file_path = os.path.join(output_path, file_name)
    resources_path = os.path.join(output_path, folder_name)
    response = get_page_obj(url)
    soup, data_for_download = parse_html_page(response, url, resources_path)
    if not os.path.exists(resources_path) and data_for_download:
        logger.info('Creating {}'.format(resources_path))
        create_directory(resources_path)
    bar = ChargingBar('Downloading resources:', max=len(data_for_download))
    for res_url, res_path in data_for_download.items():
        file_obj = download_resource_item(res_url)
        save_file(res_path, file_obj)
    bar.finish()
    save_bs_object(file_path, soup, 'w')
    return file_path
