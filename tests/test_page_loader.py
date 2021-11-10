import unittest.mock
import tempfile
import os


from tests.fake_response import FakeResponse
from page_loader.page_loader import (
    get_content_folder_name,
    download, get_name_from_url
)


def read_file(path, mode):
    with open(path, mode) as f:
        return f.read()


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
    def mock_side_effect(url, *args, **kwargs):
        if url.endswith('.png'):
            return FakeResponse(
                content=read_file('tests/fixtures/reactjs.png', 'rb')
            )
        return FakeResponse(text=read_file('tests/fixtures/test.html', 'r'))

    with unittest.mock.patch('requests.get') as mock_request:
        mock_request.side_effect = mock_side_effect
        with tempfile.TemporaryDirectory() as tmpdirname:
            assert download(
                tmpdirname, 'https://nosuchsite0kdskjdaf.com'
            ) == os.path.join(tmpdirname, 'nosuchsite0kdskjdaf-com.html')
            assert os.path.exists(tmpdirname + '/nosuchsite0kdskjdaf-com.html')
            assert os.path.exists(tmpdirname + '/nosuchsite0kdskjdaf-com_files')
            assert os.path.exists(
                tmpdirname + '/nosuchsite0kdskjdaf-com_files/reactjs.png'
            )
            img1 = read_file('tests/fixtures/reactjs.png', 'rb')
            img2 = read_file(
                tmpdirname + '/nosuchsite0kdskjdaf-com_files/reactjs.png',
                'rb'
            )
            assert img1 == img2
