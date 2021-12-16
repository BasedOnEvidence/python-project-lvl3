import os
from page_loader.logger import get_logger


logger = get_logger(__name__)


def save_file(path, file, mode='wb'):
    try:
        with open(path, mode) as f:
            if mode == 'w':
                f.write(file.prettify())
            else:
                f.write(file)
            logger.info('{} is created'.format(path))
    except OSError as err:
        logger.error(err)
        raise OSError


def create_directory(path):
    try:
        os.makedirs(path)
        logger.info('{} is created'.format(path))
    except OSError as err:
        logger.error(err)
