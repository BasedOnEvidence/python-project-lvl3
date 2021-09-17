import unittest.mock
import tempfile

from page_loader.page_loader import (
    get_content_folder_name,
    download, get_name_from_url
)


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


def test_get_content_folder_name():
    assert get_content_folder_name(
        'ru-hexlet-io-courses.html'
    ) == 'ru-hexlet-io-courses_files'
    assert get_content_folder_name(
        'ru-hexlet-io-courses.php'
    ) == 'ru-hexlet-io-courses_files'
    assert get_content_folder_name(
        '1.txt'
    ) == '1_files'


def test_download():
    with unittest.mock.patch('requests.Response.text') as mock_request:
        mock_request.return_value = open('tests/fixtures/test.html')
        # assert mock_request.return_value == download(
        #     '/var/tmp', 'https://ru.hexlet.io/courses'
        # )
    with tempfile.TemporaryDirectory() as tmpdirname:
        assert download(
            tmpdirname, 'https://ru.hexlet.io/courses'
        ) == tmpdirname + '/ru-hexlet-io-courses.html'
