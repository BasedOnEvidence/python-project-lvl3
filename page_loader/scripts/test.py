def read_file(path, mode):
    with open(path, mode) as f:
        return f.read()


def main():
    print(read_file('tests/fixtures/test.html', 'r'))


if __name__ == '__main__':
    main()
