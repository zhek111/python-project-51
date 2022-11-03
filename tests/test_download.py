import os
import pytest
import requests
from tests import get_fixture_path, read_file
from page_loader import download

FIXTURES_HEXLET_IO = [
    {
        'path_file': (
            'expected',
            'ru-hexlet-io-courses_files',
            'ru-hexlet-io-lessons.rss'),
        'url': 'https://ru.hexlet.io/about/lessons.rss'
    },
    {
        'path_file': (
            'expected',
            'ru-hexlet-io-courses_files',
            'ru-hexlet-io-courses.html'),
        'url': 'https://ru.hexlet.io/courses'
    }
]
FIXTURES_SITE_COM = [
    {
        'path_file': (
            'expected',
            'site-com-blog-about_files',
            'site-com-blog-about-assets-styles.css'),
        'url': 'https://site.com/blog/about/assets/styles.css'
    },
    {
        'path_file': (
            'expected',
            'site-com-blog-about_files',
            'site-com-blog-about.html'),
        'url': 'https://site.com/blog/about'
    },
    {
        'path_file': (
            'expected',
            'site-com-blog-about_files',
            'site-com-photos-me.jpg'),
        'url': 'https://site.com/photos/me.jpg'
    },
    {
        'path_file': (
            'expected',
            'site-com-blog-about_files',
            'site-com-assets-scripts.js'),
        'url': 'https://site.com/assets/scripts.js'
    }
]


def test_non_existent_directory(requests_mock):
    with pytest.raises(FileNotFoundError):
        data = read_file('tests/fixtures/ru-hexlet-io-courses.html')
        requests_mock.get('https://ru.hexlet.io/courses', text=data)
        download('https://ru.hexlet.io/courses', '/undefined')


def test_non_existent_site(requests_mock):
    with pytest.raises(Exception):
        requests_mock.get(
            'https://ru.hexlettt.io/courses',
            exc=requests.RequestException)
        download('https://ru.hexlettt.io/courses')


@pytest.mark.parametrize(
    "fixtures, site, file, dir, count_files",
    [
        pytest.param(
            FIXTURES_HEXLET_IO,
            'https://ru.hexlet.io/courses',
            'ru-hexlet-io-courses.html',
            'ru-hexlet-io-courses_files',
            2,
            id="hexlet_io"
        ),
        pytest.param(
            FIXTURES_SITE_COM,
            'https://site.com/blog/about',
            'site-com-blog-about.html',
            'site-com-blog-about_files',
            4,
            id="site_com"
        )
    ]
)
def test_download(
        fixtures,
        site,
        file,
        dir,
        count_files,
        tmp_path,
        requests_mock):
    for fixture in fixtures:
        expected_fixture_content = get_fixture_path(*fixture['path_file'])
        data_content = read_file(expected_fixture_content, 'rb')
        requests_mock.get(fixture['url'], content=data_content)

    expected_html = get_fixture_path('expected', file)
    correct_data = read_file(expected_html)

    initial_file_html = get_fixture_path(file)
    initial_data = read_file(initial_file_html)

    requests_mock.get(site, text=initial_data)

    recieved_path_after_download = download(site, tmp_path)
    data_after_download = read_file(recieved_path_after_download)

    count_files = len(next(os.walk(get_fixture_path(tmp_path, dir)))[2])
    assert data_after_download == correct_data
    assert count_files == count_files
