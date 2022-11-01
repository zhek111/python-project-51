import os
import pytest
import requests
from tests import get_fixture_path, read_file
from page_loader import download

LOCALHOST_FIXTURES = [
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
    }]


def test_non_existent_directory(requests_mock):
    with pytest.raises(FileNotFoundError):
        data = read_file('tests/fixtures/initial.html')
        requests_mock.get('https://ru.hexlet.io/courses', text=data)
        download('https://ru.hexlet.io/courses', '/undefined')


def test_non_existent_site(requests_mock):
    with pytest.raises(Exception):
        requests_mock.get('https://ru.hexlettt.io/courses',
                          exc=requests.RequestException)
        download('https://ru.hexlettt.io/courses')


def test_download(tmp_path, requests_mock):
    expected_fixture_rss = get_fixture_path(
        'expected', 'ru-hexlet-io-courses_files',
        'ru-hexlet-io-lessons.rss')
    data_rss = read_file(expected_fixture_rss, 'rb')
    requests_mock.get(
        'https://ru.hexlet.io/about/lessons.rss',
        content=data_rss)
    correct_data = read_file(
        get_fixture_path('expected', 'html_after_download.html'))
    initial_data = read_file(get_fixture_path('initial.html'))
    requests_mock.get('https://ru.hexlet.io/courses', text=initial_data)
    recieved_path_after_download = download(
        'https://ru.hexlet.io/courses', tmp_path)
    data_after_download = read_file(recieved_path_after_download)
    count_files = len(next(os.walk(
        get_fixture_path(tmp_path, 'ru-hexlet-io-courses_files')))[2])
    assert correct_data == data_after_download
    assert count_files == 2


def test_download3(tmp_path, requests_mock):
    for fixture in LOCALHOST_FIXTURES:
        expected_fixture_content = get_fixture_path(*fixture['path_file'])
        data_content = read_file(expected_fixture_content, 'rb')
        requests_mock.get(fixture['url'], content=data_content)

    expected_html = get_fixture_path('expected', 'site-com-blog-about.html')
    correct_data = read_file(expected_html)

    initial_file_html = get_fixture_path('site-com-blog-about.html')
    initial_data = read_file(initial_file_html)
    requests_mock.get('https://site.com/blog/about', text=initial_data)

    recieved_path_after_download = download('https://site.com/blog/about',
                                            tmp_path)
    data_after_download = read_file(recieved_path_after_download)
    count_files = len(next(os.walk(
        get_fixture_path(tmp_path, 'site-com-blog-about_files')))[2])
    assert data_after_download == correct_data
    assert count_files == 4
