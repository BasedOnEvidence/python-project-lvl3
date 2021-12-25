import os
from page_loader.logger import get_logger


logger = get_logger(__name__)


def save_file(path, file, mode='wb'):
    with open(path, mode) as f:
        if mode == 'w':
            f.write(file.prettify())
        else:
            f.write(file)
        logger.info('{} is created'.format(path))


def create_directory(path):
    os.mkdir(path)
    logger.info('{} is created'.format(path))
