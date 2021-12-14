import os
from urllib.parse import urljoin, urlparse
from page_loader.logger import get_logger


logger = get_logger(__name__)


def make_url_absolute(base_url, url):
    return urljoin(base_url, url)


def get_resources_path(file_path):
    _, ext = os.path.splitext(file_path)
    base_path, file_name = os.path.split(file_path)
    return os.path.join(base_path, file_name.replace(ext, '_files'))


def get_domain_from_url(url):
    return urlparse(url).netloc


def is_url_in_domain(domain, url):
    url_domain = get_domain_from_url(url)
    if url_domain == '' or url_domain == domain:
        return True
    return False
