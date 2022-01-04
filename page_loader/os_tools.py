import os
import logging


def save_file(path, file, mode='wb'):
    with open(path, mode) as f:
        f.write(file)
    logging.debug('{} is created'.format(path))


def test_access(path):
    if not os.access(path, os.W_OK):
        logging.error('Access denied to {}'.format(path))
        raise PermissionError
    if not os.path.exists(path):
        logging.error('No such file or directory: {}'.format(path))
        raise FileNotFoundError
    return True
