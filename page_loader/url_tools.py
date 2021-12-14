import re
from urllib.parse import urlparse
from page_loader.logger import get_logger

logger = get_logger(__name__)


def convert_url_to_file_name(url):
    parsed_url = urlparse(url)
    changed_url = re.sub(r'[\W_]', '-', parsed_url.netloc + parsed_url.path)
    logger.debug('{} converted to {}'.format(url, changed_url))
    return changed_url
