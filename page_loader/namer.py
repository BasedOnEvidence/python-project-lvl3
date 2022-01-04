import re
import os
from urllib.parse import urlparse

REGEX = r'[^A-Za-z0-9]'


def to_file_name(url, ext=''):
    if ext == '':
        url, ext = os.path.splitext(url)
        if ext == '':
            ext = '.html'
    parsed_url = urlparse(url)
    changed_url = re.sub(
        REGEX, '-', parsed_url.netloc + parsed_url.path
    ) + ext
    return changed_url


def to_dir_name(url, suffix=''):
    parsed_url = urlparse(url)
    changed_url = re.sub(
        REGEX, '-', parsed_url.netloc + parsed_url.path
    ) + suffix
    return changed_url
