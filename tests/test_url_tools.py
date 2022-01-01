from page_loader import url_tools


def test_to_file_name():
    assert url_tools.to_file_name(
        'https://ru.hexlet.io/courses', '.html'
    ) == 'ru-hexlet-io-courses.html'
    assert url_tools.to_file_name(
        'ftp://ru.hexlet.io/courses', '.html'
    ) == 'ru-hexlet-io-courses.html'
    assert url_tools.to_file_name(
        'ftp://', '.html'
    ) == '.html'
