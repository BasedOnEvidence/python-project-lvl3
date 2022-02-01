import os


def save_file(path, content):
    mode = 'w'
    if isinstance(content, bytes):
        mode = 'wb'
    with open(path, mode) as f:
        f.write(content)


def is_directory_available(path):
    if not os.path.exists(path):
        raise FileNotFoundError('No such directory: {}'.format(path))
    if os.path.isfile(path):
        raise NotADirectoryError('It is a file, not directory: {}'.format(path))
    if not os.access(path, os.W_OK):
        raise PermissionError('Access denied to {}'.format(path))
