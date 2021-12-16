import unittest.mock
import tempfile
import os
import pytest
import requests
from tests.fake_response import FakeResponse

from page_loader.page_loader import download


def read_file(path, mode):
    with open(path, mode) as f:
        return f.read()


def mock_side_effect(url, *args, **kwargs):
    if url.endswith('test-connection-error.ttttt'):
        return FakeResponse(status_code=404).raise_for_status()
    if url.endswith('.png'):
        return FakeResponse(
            content=read_file('tests/fixtures/reactjs.png', 'rb')
        )
    if url.endswith('.rss'):
        return FakeResponse(
            content=read_file('tests/fixtures/lessons.rss', 'rb')
        )
    return FakeResponse(text=read_file('tests/fixtures/test.html', 'r'))


def test_download():
    with unittest.mock.patch('requests.get') as mock_request:
        mock_request.side_effect = mock_side_effect
        with tempfile.TemporaryDirectory() as tmpdirname:
            assert download(
                'https://nosuchsite0kdskjdaf.com', tmpdirname
            ) == os.path.join(tmpdirname, 'nosuchsite0kdskjdaf-com.html')
            assert os.path.exists(tmpdirname + '/nosuchsite0kdskjdaf-com.html')
            assert os.path.exists(tmpdirname + '/nosuchsite0kdskjdaf-com_files')
            generated_png_path = os.path.join(
                tmpdirname,
                'nosuchsite0kdskjdaf-com_files',
                'nosuchsite0kdskjdaf-com-assets-professions-reactjs.png'
            )
            generated_rss_path = os.path.join(
                tmpdirname,
                'nosuchsite0kdskjdaf-com_files',
                'nosuchsite0kdskjdaf-com-assets-professions-lessons.rss'
            )
            assert os.path.exists(generated_png_path)
            assert os.path.exists(generated_rss_path)
            expected_img = read_file('tests/fixtures/reactjs.png', 'rb')
            img = read_file(generated_png_path, 'rb')
            assert img == expected_img
            expected_rss = read_file('tests/fixtures/lessons.rss', 'rb')
            rss = read_file(generated_rss_path, 'rb')
            assert rss == expected_rss
            expected_html_file = read_file('tests/fixtures/result.html', 'r')
            html_file = read_file(
                tmpdirname + '/nosuchsite0kdskjdaf-com.html', 'r'
            )
            assert html_file == expected_html_file


def test_exception_connection_error():
    with unittest.mock.patch('requests.get') as mock_request:
        mock_request.side_effect = mock_side_effect
        with pytest.raises(requests.exceptions.RequestException):
            with tempfile.TemporaryDirectory() as tmpdirname:
                download('https://test-connection-error.ttttt', tmpdirname)
