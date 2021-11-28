import tempfile
import os


from page_loader.tools import (
    get_content_folder_name,
    get_file_name_from_url,
    create_directory,
    convert_url_to_file_name,
    get_domain_from_url,
    is_url_in_domain
)


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


def test_create_directory():
    with tempfile.TemporaryDirectory() as tmpdirname:
        create_directory(tmpdirname + '/sdfs/dfs/dssd.jnf')
        assert os.path.exists(tmpdirname + '/sdfs')
        assert os.path.exists(tmpdirname + '/sdfs/dfs')
        assert not os.path.isfile(tmpdirname + '/sdfs/dfs/dssd.jnf')
        assert not os.path.exists(tmpdirname + '/sdfs/dfs/dssd.jnf')


def test_get_file_name_from_url():
    assert get_file_name_from_url(
        'https://cdn2.hexlet.io/assets/favicon-342.ico'
    ) == 'favicon-342.ico'
    assert get_file_name_from_url(
        'https://cdn2.hexlet.io/assets/favicon-342'
    ) == 'favicon-342'


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
