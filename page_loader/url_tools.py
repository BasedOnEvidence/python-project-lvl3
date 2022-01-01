import re
import os
from urllib.parse import urljoin, urlparse
from page_loader.logger import get_logger

REGEX = r'[^A-Za-z0-9]'

logger = get_logger(__name__)


def to_file_name(url, ext=''):
    if ext == '':
        url, ext = os.path.splitext(url)
        if ext == '':
            ext = '.html'
    parsed_url = urlparse(url)
    changed_url = re.sub(
        REGEX, '-', parsed_url.netloc + parsed_url.path
    ) + ext
    logger.debug('{} converted to {}'.format(url, changed_url))
    return changed_url


def to_dir_name(url, suffix=''):
    parsed_url = urlparse(url)
    changed_url = re.sub(
        REGEX, '-', parsed_url.netloc + parsed_url.path
    ) + suffix
    return changed_url


def join(original_url, url):
    parsed_url = urlparse(url)
    parsed_original_url = urlparse(original_url)
    base = parsed_original_url.scheme + '://' + parsed_original_url.netloc
    if parsed_url.scheme:
        return url
    if parsed_url.path.startswith('/'):
        return urljoin(base, parsed_url.path)
    return urljoin(base, os.path.join(parsed_original_url.path, url))


def get_netloc(url):
    return urlparse(url).netloc
