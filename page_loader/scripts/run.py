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
        print(download(args.link, args.output))
    except requests.exceptions.RequestException as err:
        logger.error(err)
        sys.exit(1)
    except OSError as err:
        logger.error(err)
        sys.exit(1)


if __name__ == '__main__':
    main()
