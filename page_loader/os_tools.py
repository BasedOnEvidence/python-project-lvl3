from page_loader.logger import get_logger


WRITE_MODE_EXT = ['.html', '.txt', '.css']

logger = get_logger(__name__)


def save_file(path, file, mode='wb'):
    with open(path, mode) as f:
        f.write(file)
    logger.debug('{} is created'.format(path))
