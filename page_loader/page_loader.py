import os
import logging
import requests
from progress.bar import ChargingBar
from page_loader import url_formatter
from page_loader.resources import process_html
from page_loader.storage import (
    save_file,
    is_directory_available
)


def make_request(url):
    response = requests.get(url)
    response.raise_for_status()
    return response


def download_resource_item(url, path):
    try:
        response = make_request(url)
        res_file_name = url_formatter.to_file_name(url)
        res_file_path = os.path.join(path, res_file_name)
        save_file(res_file_path, response.content)
    except requests.HTTPError as err:
        logging.warning(str(err))
    return response.content


def download(url, output_path):
    logging.info('Program started')
    is_directory_available(output_path)
    file_path = os.path.join(output_path, url_formatter.to_file_name(url))
    res_path = os.path.join(output_path, url_formatter.to_dir_name(url))
    response = make_request(url)
    html, resources = process_html(response, url)
    save_file(file_path, html)
    if not os.path.exists(res_path) and resources:
        os.mkdir(res_path)
    bar = ChargingBar('Downloading resources:', max=len(resources))
    for res_url in resources:
        download_resource_item(res_url, res_path)
        bar.next()
    bar.finish()
    logging.info('The program completed successfully')
    return file_path
