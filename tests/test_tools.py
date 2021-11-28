import tempfile
import os


from page_loader.tools import (
    get_content_folder_name,
    get_file_name_from_url,
    create_path_if_it_is_not_exists
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


def test_create_path_if_it_is_not_exists():
    with tempfile.TemporaryDirectory() as tmpdirname:
        create_path_if_it_is_not_exists(tmpdirname + '/sdfs/dfs/dssd.jnf')
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
