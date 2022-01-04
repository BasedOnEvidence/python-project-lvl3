import re
import os
from urllib.parse import urlparse

REGEX = r'[^A-Za-z0-9]'


def to_file_name(url, force_ext=''):
    if force_ext != '_files' and force_ext == '':
        url, force_ext = os.path.splitext(url)
        if force_ext == '':
            force_ext = '.html'
        if not force_ext.startswith('.'):
            force_ext = '.' + force_ext
    parsed_url = urlparse(url)
    changed_url = re.sub(
        REGEX, '-', parsed_url.netloc + parsed_url.path
    ) + force_ext
    return changed_url


def to_dir_name(url, suffix='_files'):
    return to_file_name(url, suffix)
