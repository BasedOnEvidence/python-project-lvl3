from page_loader import namer


def test_to_file_name():
    assert namer.to_file_name(
        'https://ru.hexlet.io/courses', '.html'
    ) == 'ru-hexlet-io-courses.html'
    assert namer.to_file_name(
        'ftp://ru.hexlet.io/courses', '.html'
    ) == 'ru-hexlet-io-courses.html'
    assert namer.to_file_name(
        'ftp://', '.html'
    ) == '.html'
