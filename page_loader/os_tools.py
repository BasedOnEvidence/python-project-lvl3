import logging

WRITE_MODE_EXT = ['.html', '.txt', '.css']

logger = logging.getLogger(__name__)


def save_file(path, file, mode='wb'):
    with open(path, mode) as f:
        f.write(file)
    logger.debug('{} is created'.format(path))
