from page_loader.cli import get_args_parser
from page_loader.page_loader import download


def main():
    parser = get_args_parser()
    args = parser.parse_args()
    file_path = download(args.output, args.link)
    print(file_path)


if __name__ == '__main__':
    main()
