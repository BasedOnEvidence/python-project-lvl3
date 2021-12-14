from page_loader.url_tools import convert_url_to_file_name


def test_convert_url_to_file_name():
    assert convert_url_to_file_name(
        'https://ru.hexlet.io/courses'
    ) == 'ru-hexlet-io-courses'
    assert convert_url_to_file_name(
        'ftp://ru.hexlet.io/courses'
    ) == 'ru-hexlet-io-courses'
    assert convert_url_to_file_name(
        'ftp://'
    ) == ''
