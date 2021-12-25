from page_loader.url_tools import (
    convert_url_to_file_name,
    is_urls_have_same_base
)


def test_convert_url_to_file_name():
    assert convert_url_to_file_name(
        'https://ru.hexlet.io/courses', '.html'
    ) == 'ru-hexlet-io-courses.html'
    assert convert_url_to_file_name(
        'ftp://ru.hexlet.io/courses', '.html'
    ) == 'ru-hexlet-io-courses.html'
    assert convert_url_to_file_name(
        'ftp://', '.html'
    ) == '.html'


def test_is_urls_have_same_base():
    assert is_urls_have_same_base(
        'https://ru.hexlet.io', 'https://ru.hexlet.io/courses'
    ) is True
    assert is_urls_have_same_base(
        'https://ru.hexlet.io', 'https://www.ru.hexlet.io/courses'
    ) is False
    assert is_urls_have_same_base(
        'https://ru.dsfsdfs.rrejek', 'http://www.ger.ru/courses'
    ) is False
