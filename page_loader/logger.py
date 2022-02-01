import logging


LOG_FORMAT = '[(%(levelname)s)-%(asctime)s-%(name)s]: %(message)s'


def setup(level):
    logging.basicConfig(
        format=LOG_FORMAT,
        level=level,
        encoding='utf-8'
    )
