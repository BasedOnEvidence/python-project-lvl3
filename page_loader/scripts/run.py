import sys
import requests

from page_loader.cli import get_args_parser
from page_loader.page_loader import download
from page_loader.logger import get_logger


logger = get_logger(__name__)


def main():
    parser = get_args_parser()
    args = parser.parse_args()
    try:
        download(args.link, args.output)
    except requests.exceptions.ConnectionError as err:
        logger.error('Connection error: {}'.format(err))
        sys.exit(1)
    except FileNotFoundError as err:
        logger.error('No such directory: {}'.format(err))
        sys.exit(1)
    except FileExistsError as err:
        logger.error('File already downloaded: {}'.format(err))
        sys.exit(1)
    except Exception as err:
        logger.error(err)
        sys.exit(1)


if __name__ == '__main__':
    main()
