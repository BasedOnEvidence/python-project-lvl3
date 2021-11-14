import os
import errno


def create_path_if_it_is_not_exists(path):
    if not os.path.exists(os.path.dirname(path)):
        try:
            os.makedirs(os.path.dirname(path))
        except OSError as err:
            if err.errno != errno.EEXIST:
                raise


def get_content_folder_name(file_name):
    _, ext = os.path.splitext(file_name)
    return file_name.replace(ext, '_files')


def get_file_name_from_url(url):
    return os.path.basename(url)
