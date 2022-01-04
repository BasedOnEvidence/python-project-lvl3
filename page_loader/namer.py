import re
import os
from urllib.parse import urlparse

FORMAT_URL_PATTERN = r'[^A-Za-z0-9]'


def get_ext(url):
    url, ext = os.path.splitext(url)
    if ext == '':
        ext = '.html'
    if not ext.startswith('.'):
        ext = '.' + ext
    return ext


def to_file_name(url, force_ext=''):
    if force_ext == '':
        force_ext = get_ext(url)
    parsed_url = urlparse(url)
    changed_url = re.sub(
        FORMAT_URL_PATTERN, '-', parsed_url.netloc + parsed_url.path
    ) + force_ext
    return changed_url


def to_dir_name(url, suffix='_files'):
    return to_file_name(url, suffix)
