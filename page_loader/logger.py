import logging


log_format = '[(%(levelname)s)-%(asctime)s-%(name)s]: %(message)s'


def setup(level):
    logging.basicConfig(
        format=log_format,
        level=level,
        encoding='utf-8'
    )
