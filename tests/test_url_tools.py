from page_loader import namer


def test_convert_url_to_file_name():
    assert namer.to_file_name(
        'https://ru.hexlet.io/courses', '.html'
    ) == 'ru-hexlet-io-courses.html'
    assert namer.to_file_name(
        'ftp://ru.hexlet.io/courses', '.html'
    ) == 'ru-hexlet-io-courses.html'
    assert namer.to_file_name(
        'ftp://', '.html'
    ) == '.html'


def test_convert_url_to_dir_name():
    assert namer.to_dir_name(
        'https://ru.hexlet.io/courses', '_files'
    ) == 'ru-hexlet-io-courses_files'
    assert namer.to_dir_name(
        'ftp://ru.hexlet.io/courses'
    ) == 'ru-hexlet-io-courses_files'
