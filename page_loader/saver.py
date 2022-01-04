import os


def save_content(path, file):
    mode = 'w'
    if isinstance(file, bytes):
        mode = 'wb'
    with open(path, mode) as f:
        f.write(file)


def is_writable(path):
    if not os.access(path, os.W_OK):
        raise PermissionError('Access denied to {}'.format(path))
    if not os.path.exists(path) or os.path.isfile(path):
        raise FileNotFoundError('No such directory: {}'.format(path))
    return True
