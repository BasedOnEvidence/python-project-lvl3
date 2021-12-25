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
    if url.endswith('connection-err.com'):
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
                'https://test.com', tmpdirname
            ) == os.path.join(tmpdirname, 'test-com.html')
            assert os.path.exists(tmpdirname + '/test-com.html')
            assert os.path.exists(tmpdirname + '/test-com_files')
            generated_png_path = os.path.join(
                tmpdirname,
                'test-com_files',
                'test-com-assets-professions-reactjs.png'
            )
            generated_rss_path = os.path.join(
                tmpdirname,
                'test-com_files',
                'test-com-assets-professions-lessons.rss'
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
                tmpdirname + '/test-com.html', 'r'
            )
            assert html_file == expected_html_file


def test_exceptions():
    with unittest.mock.patch('requests.get') as mock_request:
        mock_request.side_effect = mock_side_effect
        with tempfile.TemporaryDirectory() as tmpdirname:
            with pytest.raises(requests.exceptions.RequestException):
                download('https://connection-err.com', tmpdirname)
            assert not os.path.exists(tmpdirname + '/connection-err-com.html')
            assert not os.path.exists(tmpdirname + '/connection-err-com_files')
            with pytest.raises(PermissionError):
                os.chmod(tmpdirname, 0o444)
                download('https://test.com', tmpdirname)
            with pytest.raises(FileNotFoundError):
                os.rmdir(os.path.basename(tmpdirname))
                download('https://test.com', tmpdirname)
            assert not os.path.exists(tmpdirname + '/test-com.html')
            assert not os.path.exists(tmpdirname + '/test-com_files')
