import re
import os
from urllib.parse import urlparse
from page_loader.logger import get_logger

SCHEME = 'http'
logger = get_logger(__name__)


def convert_url_to_file_name(url):
    parsed_url = urlparse(url)
    changed_url = re.sub(r'[\W_]', '-', parsed_url.netloc + parsed_url.path)
    logger.debug('{} converted to {}'.format(url, changed_url))
    return changed_url


def main():
    print(convert_url_to_file_name('https://ru.hexlet.io/courses/reactjs'))
    print(
        os.path.join(
            '123',
            'nosuchsite0kdskjdaf-com_files',
            'nosuchsite0kdskjdaf-com-assets-professions-reactjs.png'
        )
    )


if __name__ == '__main__':
    main()
