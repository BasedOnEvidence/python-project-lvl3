import os
from urllib.parse import urlparse
import re


def get_file_name_from_url(url):
    return os.path.basename(url)


def make_url_absolute(base_url, url):
    if 'http' not in url:
        return base_url + url
    return url


def get_resources_path(file_path):
    _, ext = os.path.splitext(file_path)
    base_path, file_name = os.path.split(file_path)
    return os.path.join(base_path, file_name.replace(ext, '_files'))


def convert_url_to_html_path(url, output_path):
    result = re.split(r'//', url)[1]
    result = re.sub(r'\W', '-', result)
    result += '.html'
    result = os.path.join(output_path, result)
    return result


def get_domain_from_url(url):
    return urlparse(url).netloc


def is_url_in_domain(domain, url):
    url_domain = get_domain_from_url(url)
    if url_domain == '' or url_domain == domain:
        return True
    return False
