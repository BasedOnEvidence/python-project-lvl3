import logging
import sys

from page_loader import logger
from page_loader.cli import get_args_parser
from page_loader.page_loader import download


def main():
    parser = get_args_parser()
    args = parser.parse_args()
    logger.setup(args.log_level)
    try:
        print(download(args.link, args.output))
    except Exception as err:
        logging.error(str(err))
        logging.debug('', exc_info=True)
        sys.exit(1)


if __name__ == '__main__':
    main()
