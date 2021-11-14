import unittest.mock
import tempfile
import os


from tests.fake_response import FakeResponse

from page_loader.page_loader import (
    download,
    convert_url_to_file_name
)


def read_file(path, mode):
    with open(path, mode) as f:
        return f.read()


def test_get_name_from_url():
    assert convert_url_to_file_name(
        'https://ru.hexlet.io/courses'
    ) == 'ru-hexlet-io-courses.html'
    assert convert_url_to_file_name(
        'ftp://ru.hexlet.io/courses'
    ) == 'ru-hexlet-io-courses.html'
    assert convert_url_to_file_name(
        'ftp://'
    ) == '.html'


def test_download():
    def mock_side_effect(url, *args, **kwargs):
        if url.endswith('.png'):
            return FakeResponse(
                content=read_file('tests/fixtures/reactjs.png', 'rb')
            )
        if url.endswith('.rss'):
            return FakeResponse(
                content=read_file('tests/fixtures/lessons.rss', 'rb')
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
            rss_path = tmpdirname + '/nosuchsite0kdskjdaf-com_files/lessons.rss'
            png_path = tmpdirname + '/nosuchsite0kdskjdaf-com_files/reactjs.png'
            assert os.path.exists(
                tmpdirname + '/nosuchsite0kdskjdaf-com_files/reactjs.png'
            )
            assert os.path.exists(
                tmpdirname + '/nosuchsite0kdskjdaf-com_files/lessons.rss'
            )
            img1 = read_file('tests/fixtures/reactjs.png', 'rb')
            img2 = read_file(
                tmpdirname + '/nosuchsite0kdskjdaf-com_files/reactjs.png',
                'rb'
            )
            assert img1 == img2
            rss1 = read_file('tests/fixtures/lessons.rss', 'rb')
            rss2 = read_file(
                tmpdirname + '/nosuchsite0kdskjdaf-com_files/lessons.rss',
                'rb'
            )
            assert rss1 == rss2
            html_file = read_file(
                tmpdirname + '/nosuchsite0kdskjdaf-com.html', 'r'
            )
            assert rss_path in html_file
            assert png_path in html_file
