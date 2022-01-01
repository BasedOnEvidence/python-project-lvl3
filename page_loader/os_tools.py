import os
from page_loader.logger import get_logger

WRITE_MODE_EXT = ['.html', '.txt']

logger = get_logger(__name__)


def save_file(path, file, mode='wb'):
    ext = os.path.splitext(path)[1]
    if ext in WRITE_MODE_EXT:
        mode = 'w'
    with open(path, mode) as f:
        f.write(file)
    logger.debug('{} is created'.format(path))
