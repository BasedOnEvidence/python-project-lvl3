import re
import os
from urllib.parse import urlparse

FORMAT_URL_PATTERN = r'[^A-Za-z0-9]'


def to_result_name(netloc, path, ext):
    return re.sub(FORMAT_URL_PATTERN, '-', netloc + path) + ext


def to_file_name(url, force_ext=''):
    url_path = urlparse(url).path
    url_netlock = urlparse(url).netloc
    if force_ext == '':
        url_path, force_ext = os.path.splitext(url_path)
        if force_ext == '':
            force_ext = '.html'
    elif not force_ext.startswith('.'):
        force_ext = '.' + force_ext
    return to_result_name(url_netlock, url_path, force_ext)


def to_dir_name(url, suffix='_files'):
    return to_result_name(urlparse(url).netloc, urlparse(url).path, suffix)
