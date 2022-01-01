import sys
import logging

from page_loader.cli import get_args_parser
from page_loader.page_loader import download
from page_loader.logger import set_log_settings


logger = logging.getLogger(__name__)


def main():
    parser = get_args_parser()
    args = parser.parse_args()
    set_log_settings(args.log_level)
    try:
        print(download(args.link, args.output))
        sys.exit(0)
    except Exception as err:
        logger.error(str(err))
        logger.debug(exc_info=True)
        sys.exit(1)


if __name__ == '__main__':
    main()
