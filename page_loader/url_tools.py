import re
import os
from urllib.parse import urlparse, urlunparse
from page_loader.logger import get_logger

logger = get_logger(__name__)


def convert_url_to_file_name(url):
    parsed_url = urlparse(url)
    changed_url = re.sub(r'[\W_]', '-', parsed_url.netloc + parsed_url.path)
    logger.debug('{} converted to {}'.format(url, changed_url))
    return changed_url


def convert_url_to_standart_view(url, original_url):
    parsed_url = urlparse(url)
    parsed_original_url = urlparse(original_url)
    if parsed_url.scheme:
        return url
    if parsed_url.path.startswith('/'):
        return urlunparse((
            parsed_original_url.scheme,
            parsed_original_url.netloc,
            parsed_url.path,
            '', '', ''
        ))
    return urlunparse((
        parsed_original_url.scheme,
        parsed_original_url.netloc,
        os.path.join(parsed_original_url.path, url),
        '', '', ''
    ))


def is_url_in_domain(url, original_url):
    parsed_url = urlparse(url)
    parsed_original_url = urlparse(original_url)
    logger.debug(
        'Checking is url {} in {}'.format(parsed_url, parsed_original_url)
    )
    if parsed_url.netloc == parsed_original_url.netloc:
        return True
    return False
