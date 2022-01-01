import sys

from page_loader.cli import get_args_parser
from page_loader.page_loader import download
from page_loader.logger import get_logger


logger = get_logger(__name__)


def main():
    parser = get_args_parser()
    args = parser.parse_args()
    try:
        print(download(args.link, args.output))
        sys.exit(0)
    except PermissionError as err:
        logger.error('Access denied. ' + str(err), exc_info=True)
        sys.exit(3)
    except FileNotFoundError as err:
        logger.error('Not found. ' + str(err), exc_info=True)
        sys.exit(4)
    except Exception as err:
        logger.error(str(err), exc_info=True)
        sys.exit(1)


if __name__ == '__main__':
    main()
