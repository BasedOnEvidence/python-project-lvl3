import argparse


def get_args_parser():
    parser = argparse.ArgumentParser(description='Page loader')
    parser.add_argument(
        '-o',
        '--output',
        default='/var/tmp',
        help='set format of output'
    )
    log_level_choices = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    parser.add_argument(
        '-l',
        '--log_level',
        default='WARNING',
        type=str.upper,
        choices=log_level_choices,
        help='set log level',
    )
    parser.add_argument('link')
    return parser
