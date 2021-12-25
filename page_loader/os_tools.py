import os
from page_loader.logger import get_logger


logger = get_logger(__name__)


def save_bs_object(path, file, mode='w'):
    with open(path, mode) as f:
        f.write(file.prettify())
    logger.info('{} is created'.format(path))


def save_file(path, file, mode='wb'):
    with open(path, mode) as f:
        f.write(file)
    logger.info('{} is created'.format(path))


def create_directory(path):
    os.mkdir(path)
    logger.info('{} is created'.format(path))
