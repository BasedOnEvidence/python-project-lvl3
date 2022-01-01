import mimetypes
from page_loader.logger import get_logger

WRITE_MODE_EXT = ['.html', '.txt']

logger = get_logger(__name__)


def save_file(path, file):
    file_type = mimetypes.guess_type(path)[0]
    if file_type and 'text' in file_type:
        mode = 'w'
    else:
        mode = 'wb'
    with open(path, mode) as f:
        f.write(file)
    logger.debug('{} is created'.format(path))
