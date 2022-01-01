import logging


_log_format = '[(%(levelname)s)-%(asctime)s-%(name)s]: %(message)s'


def set_log_settings(level):
    logging.basicConfig(
        format=_log_format,
        level=level,
        encoding='utf-8'
    )
