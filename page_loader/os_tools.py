from page_loader.logger import get_logger


WRITE_MODE_EXT = ['.html', '.txt', '.css']

logger = get_logger(__name__)


def save_file(path, file, mode='wb'):
    try:
        with open(path, mode) as f:
            f.write(file)
        logger.debug('{} is created'.format(path))
    except FileNotFoundError as err:
        logger.error('No such file or directory!')
        raise FileNotFoundError(err)
    except PermissionError as err:
        logger.error('Access denied!')
        raise PermissionError(err)
