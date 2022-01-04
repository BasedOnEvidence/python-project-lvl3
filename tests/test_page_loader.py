import tempfile
import os
import pytest
import requests
import unittest.mock
from tests.fake_response import FakeResponse
from page_loader.page_loader import download


def read_file(path, mode='rb'):
    ext = os.path.splitext(path)[1]
    if ext == '.html':
        mode = 'r'
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


def assert_content(path1, path2):
    content1 = read_file(path1)
    content2 = read_file(path2)
    assert content1 == content2


def test_download():
    with unittest.mock.patch('requests.get') as mock_request:
        mock_request.side_effect = mock_side_effect
        with tempfile.TemporaryDirectory() as tmpdir:
            assert download(
                'https://test.com', tmpdir
            ) == os.path.join(tmpdir, 'test-com.html')
            assert os.path.exists(os.path.join(tmpdir, 'test-com.html'))
            assert os.path.exists(os.path.join(tmpdir, 'test-com_files'))
            png_path = os.path.join(
                tmpdir,
                'test-com_files',
                'test-com-assets-professions-reactjs.png'
            )
            rss_path = os.path.join(
                tmpdir,
                'test-com_files',
                'test-com-assets-professions-lessons.rss'
            )
            assert os.path.exists(png_path)
            assert os.path.exists(rss_path)
            assert_content(
                png_path,
                'tests/fixtures/reactjs.png'
            )
            assert_content(
                rss_path,
                'tests/fixtures/lessons.rss'
            )
            assert_content(
                os.path.join(tmpdir, 'test-com.html'),
                'tests/fixtures/result.html'
            )


def test_connection_exception():
    with unittest.mock.patch('requests.get') as mock_request:
        mock_request.side_effect = mock_side_effect
        with tempfile.TemporaryDirectory() as tmpdir:
            with pytest.raises(requests.exceptions.RequestException):
                download('https://connection-err.com', tmpdir)
            assert not os.path.exists(
                os.path.join(tmpdir, 'connection-err-com.html')
            )
            assert not os.path.exists(
                os.path.join(tmpdir, 'connection-err-com_files')
            )


def test_permission_exception():
    with unittest.mock.patch('requests.get') as mock_request:
        mock_request.side_effect = mock_side_effect
        with tempfile.TemporaryDirectory() as tmpdir:
            with pytest.raises(PermissionError):
                os.chmod(tmpdir, 0o444)
                download('https://test.com', tmpdir)
            assert not os.path.exists(os.path.join(tmpdir, 'test-com.html'))
            assert not os.path.exists(os.path.join(tmpdir, 'test-com_files'))


def test_file_not_found_exception():
    with unittest.mock.patch('requests.get') as mock_request:
        mock_request.side_effect = mock_side_effect
        with tempfile.TemporaryDirectory() as tmpdir:
            with pytest.raises(FileNotFoundError):
                os.rmdir(os.path.basename(tmpdir))
                download('https://test.com', tmpdir)
            assert not os.path.exists(os.path.join(tmpdir, 'test-com.html'))
            assert not os.path.exists(os.path.join(tmpdir, 'test-com_files'))
