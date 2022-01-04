import os
import logging
import requests
from progress.bar import ChargingBar
from page_loader.html_handler import process_html
from page_loader import name_assigner
from page_loader.requester import (
    make_request
)
from page_loader.saver import (
    save_content,
    test_access
)


def download_resource_item(url):
    try:
        response = make_request(url)
    except requests.HTTPError as err:
        logging.warning(str(err))
    return response.content


def download(url, output_path):
    file_path = os.path.join(
        output_path, name_assigner.to_file_name(url, '.html')
    )
    res_path = os.path.join(
        output_path, name_assigner.to_dir_name(url, '_files')
    )
    response = make_request(url)
    html, resources = process_html(response, url)
    test_access(output_path)
    save_content(file_path, html)
    if not os.path.exists(res_path) and resources:
        os.mkdir(res_path)
        logging.debug('{} is created'.format(res_path))
    bar = ChargingBar('Downloading resources:', max=len(resources))
    for res_url in resources:
        file_obj = download_resource_item(res_url)
        res_file_name = name_assigner.to_file_name(res_url)
        res_file_path = os.path.join(res_path, res_file_name)
        save_content(res_file_path, file_obj)
        bar.next()
    bar.finish()
    return file_path
