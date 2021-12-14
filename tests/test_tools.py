from page_loader.tools import (
    get_resources_path,
    get_domain_from_url,
    is_url_in_domain,
    make_url_absolute
)


def test_get_resources_path():
    assert get_resources_path(
        '/var/tmp/ru-hexlet-io-courses.html'
    ) == '/var/tmp/ru-hexlet-io-courses_files'
    assert get_resources_path(
        'ru-hexlet-io-courses.php'
    ) == 'ru-hexlet-io-courses_files'
    assert get_resources_path(
        '1.txt'
    ) == '1_files'


def test_get_domain_from_url():
    assert get_domain_from_url('https://ru.hexlet.io/courses') == 'ru.hexlet.io'
    assert get_domain_from_url('www.ru.hexlet.io/courses') == ''
    assert get_domain_from_url('http://www.ru') == 'www.ru'


def test_is_url_in_domain():
    assert is_url_in_domain(
        'ru.hexlet.io', 'https://ru.hexlet.io/courses'
    ) is True
    assert is_url_in_domain(
        'ru.hexlet.io', 'www.ru.hexlet.io/courses'
    ) is True
    assert is_url_in_domain(
        'ru.dsfsdfs.rrejek', 'http://www.ru/courses'
    ) is False


def test_make_url_absolute():
    assert make_url_absolute(
        'http://www.example.ru/courses', '/assets/test.rss'
    ) == 'http://www.example.ru/assets/test.rss'
