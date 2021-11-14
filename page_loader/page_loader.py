import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from page_loader.os_tools import (
    create_path_if_it_is_not_exists,
    get_content_folder_name,
    get_file_name_from_url
)


RESOURCES = {
    'img': 'src',
    'link': 'href',
    'script': 'src'
}


def convert_url_to_file_name(url):
    result = re.split(r'//', url)[1]
    result = re.sub(r'\W', '-', result)
    result += '.html'
    return result


def get_domain_from_url(url):
    return urlparse(url).netloc


def is_url_in_domain(domain, url):
    url_domain = get_domain_from_url(url)
    if url_domain == '' or url_domain == domain:
        return True
    return False


def find_content(soup: BeautifulSoup) -> dict[str, list]:
    data = {}
    for tag in RESOURCES.keys():
        tags = soup.find_all(tag, {RESOURCES[tag]: True})
        urls = [item[RESOURCES[tag]] for item in tags]
        data[tag] = urls
    return data


def download_content(txt_data, output_path, content_path, base_url):
    current_txt = txt_data
    domain = get_domain_from_url(base_url)
    urls = find_content(BeautifulSoup(txt_data, 'html.parser'))
    for tag in RESOURCES.keys():
        for url in urls[tag]:
            if is_url_in_domain(domain, url):
                print(url)
                file_name = get_file_name_from_url(url)
                content_file_path = content_path + '/' + file_name
                current_txt = current_txt.replace(url, content_file_path)
                create_path_if_it_is_not_exists(content_file_path)
                with open(content_file_path, 'wb') as f:
                    if 'http' not in url:
                        url = '{}{}'.format(base_url, url)
                    response = requests.get(url)
                    f.write(response.content)
    with open(output_path, 'w') as file_:
        file_.write(current_txt)


def download(output_path, url):
    response = requests.get(url, allow_redirects=True)
    txt_data = response.text
    file_name = convert_url_to_file_name(url)
    content_folder_name = get_content_folder_name(file_name)
    content_path = output_path + '/' + content_folder_name
    output_path += '/' + file_name
    download_content(txt_data, output_path, content_path, url)
    return output_path
