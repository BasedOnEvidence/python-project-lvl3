from page_loader import name_assigner


def test_to_file_name():
    assert name_assigner.to_file_name(
        'https://ru.hexlet.io/courses', '.html'
    ) == 'ru-hexlet-io-courses.html'
    assert name_assigner.to_file_name(
        'ftp://ru.hexlet.io/courses', '.html'
    ) == 'ru-hexlet-io-courses.html'
    assert name_assigner.to_file_name(
        'ftp://', '.html'
    ) == '.html'
