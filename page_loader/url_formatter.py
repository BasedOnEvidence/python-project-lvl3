import re
import os
from urllib.parse import urlparse

FORMAT_URL_PATTERN = r'[^A-Za-z0-9]'


def to_result_name(netloc, path, ext):
    return re.sub(FORMAT_URL_PATTERN, '-', netloc + path) + ext


def to_file_name(url, force_ext=None):
    url_path = urlparse(url).path
    url_path, ext = os.path.splitext(url_path)
    ext = force_ext or ext
    url_netlock = urlparse(url).netloc
    if not ext:
        ext = 'html'
    name = re.sub(FORMAT_URL_PATTERN, '-', url_netlock + url_path)
    return '{}.{}'.format(name, ext.lstrip('.'))


def to_dir_name(url, suffix='_files'):
    file_name, _ = os.path.splitext(to_file_name(url))
    return '{}{}'.format(file_name, suffix)
