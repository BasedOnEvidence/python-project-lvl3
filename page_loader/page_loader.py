import os
import logging
from progress.bar import ChargingBar
from page_loader.html_handler import process_html
from page_loader import url_tools
from page_loader.network_tools import (
    download_resource_item,
    make_request
)
from page_loader.os_tools import (
    save_file,
    test_access
)


def download(url, output_path):
    file_path = os.path.join(output_path, url_tools.to_file_name(url, '.html'))
    res_path = os.path.join(output_path, url_tools.to_dir_name(url, '_files'))
    response = make_request(url)
    html, resources = process_html(response, url)
    test_access(output_path)
    save_file(file_path, html, mode='w')
    if not os.path.exists(res_path) and resources:
        os.mkdir(res_path)
        logging.debug('{} is created'.format(res_path))
    bar = ChargingBar('Downloading resources:', max=len(resources))
    for res_url in resources:
        file_obj = download_resource_item(res_url)
        res_file_name = url_tools.to_file_name(res_url)
        res_file_path = os.path.join(res_path, res_file_name)
        save_file(res_file_path, file_obj)
        bar.next()
    bar.finish()
    return file_path
