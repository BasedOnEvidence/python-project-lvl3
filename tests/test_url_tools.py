from page_loader.url_tools import (
    to_file_name,
)


def test_to_file_name():
    assert to_file_name(
        'https://ru.hexlet.io/courses', '.html'
    ) == 'ru-hexlet-io-courses.html'
    assert to_file_name(
        'ftp://ru.hexlet.io/courses', '.html'
    ) == 'ru-hexlet-io-courses.html'
    assert to_file_name(
        'ftp://', '.html'
    ) == '.html'
