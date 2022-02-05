import os
import tempfile
import unittest.mock

import pytest
import requests

from page_loader.page_loader import download
from tests.fake_response import FakeResponse


def read_file(path, mode='rb'):
    with open(path, mode) as f:
        return f.read()


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


def assert_files_content(path1, path2):
    content1 = read_file(path1, 'rb')
    content2 = read_file(path2, 'rb')
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
            assert_files_content(
                png_path,
                'tests/fixtures/reactjs.png'
            )
            assert_files_content(
                rss_path,
                'tests/fixtures/lessons.rss'
            )
            assert_files_content(
                os.path.join(tmpdir, 'test-com.html'),
                'tests/fixtures/result.html'
            )


def assert_exception_raises(exception, tmpdir):
    with pytest.raises(exception):
        download('https://test.com', tmpdir)
    assert not os.path.exists(os.path.join(tmpdir, 'test-com.html'))
    assert not os.path.exists(os.path.join(tmpdir, 'test-com_files'))


def test_404_not_found():
    with unittest.mock.patch('requests.get') as mock_request:
        mock_request.side_effect = requests.HTTPError
        with tempfile.TemporaryDirectory() as tmpdir:
            assert_exception_raises(
                requests.exceptions.RequestException, tmpdir
            )


def test_access_to_dir_exception():
    with unittest.mock.patch('requests.get') as mock_request:
        mock_request.side_effect = mock_side_effect
        with tempfile.TemporaryDirectory() as tmpdir:
            os.chmod(tmpdir, 0o444)
            assert_exception_raises(PermissionError, tmpdir)


def test_dir_not_found_exception():
    with unittest.mock.patch('requests.get') as mock_request:
        mock_request.side_effect = mock_side_effect
        with tempfile.TemporaryDirectory() as tmpdir:
            assert_exception_raises(FileNotFoundError, tmpdir + 'test')
