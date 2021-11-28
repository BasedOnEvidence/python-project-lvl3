import os
import errno
from urllib.parse import urlparse
import re


def create_directory(path):
    if not os.path.exists(os.path.dirname(path)):
        try:
            os.makedirs(os.path.dirname(path))
        except OSError as err:
            if err.errno != errno.EEXIST:
                raise


def get_content_folder_name(file_name):
    _, ext = os.path.splitext(file_name)
    return file_name.replace(ext, '_files')


def get_file_name_from_url(url):
    return os.path.basename(url)


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
