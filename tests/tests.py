import os

from page_loader.page_loader import download, get_name_from_url


def test_get_name_from_url():
    assert get_name_from_url(
        'https://ru.hexlet.io/courses'
    ) == 'ru-hexlet-io-courses.html'
    assert get_name_from_url(
        'ftp://ru.hexlet.io/courses'
    ) == 'ru-hexlet-io-courses.html'
    assert get_name_from_url(
        'ftp://'
    ) == '.html'


def test_download():
    assert download(
        '/var/tmp', 'https://ru.hexlet.io/courses'
    ) == '/var/tmp/ru-hexlet-io-courses.html'
    assert os.path.isfile('/var/tmp/ru-hexlet-io-courses.html') is True
    os.remove('/var/tmp/ru-hexlet-io-courses.html')
    assert os.path.isfile('/var/tmp/ru-hexlet-io-courses.html') is False
