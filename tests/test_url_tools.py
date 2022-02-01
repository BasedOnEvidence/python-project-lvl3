import pytest
from page_loader import url_formatter


@pytest.mark.parametrize('url, ext, expected', [
    ('https://ru.hexlet.io/courses', '.html', 'ru-hexlet-io-courses.html'),
    ('ftp://site.php/courses', None, 'site-php-courses.html'),
    ('ru.hexlet.io/courses', 'html', 'ru-hexlet-io-courses.html'),
    ('ftp://', '.html', '.html')
])
def test_convert_url_to_file_name(url, ext, expected):
    assert url_formatter.to_file_name(url, ext) == expected


@pytest.mark.parametrize('url, suffix, expected', [
    ('https://ru.hexlet.io/courses', '_files', 'ru-hexlet-io-courses_files'),
    ('ftp://site.php/courses', '_courses', 'site-php-courses_courses')
])
def test_convert_url_to_dir_name(url, suffix, expected):
    assert url_formatter.to_dir_name(url, suffix) == expected
