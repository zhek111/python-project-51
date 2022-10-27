import os
import pytest
import requests
from tests import get_path
from page_loader import download
from tests.fixtures.expected.localhost import localhost_fixtures


def test_non_existent_directory(requests_mock):
    with pytest.raises(FileNotFoundError):
        with open('tests/fixtures/initial.html') as file:
            data = file.read()
            requests_mock.get('https://ru.hexlet.io/courses', text=data)
            download('https://ru.hexlet.io/courses', '/undefined')


def test_non_existent_site(requests_mock):
    with pytest.raises(Exception):
        requests_mock.get('https://ru.hexlettt.io/courses',
                          exc=requests.RequestException)
        download('https://ru.hexlettt.io/courses')


def test_download(tmp_path, requests_mock):
    with open(
            get_path('ru-hexlet-io-lessons.rss',
                     'ru-hexlet-io-courses_files'),
            'rb') as file:
        data1 = file.read()
        requests_mock.get(
            'https://ru.hexlet.io/about/lessons.rss',
            content=data1)
    file_with_download = open(get_path('with_download.html'))
    correct_data = file_with_download.read()
    with open(get_path('initial.html')) as file:
        initial_data = file.read()
    requests_mock.get('https://ru.hexlet.io/courses', text=initial_data)
    path_download_file = download('https://ru.hexlet.io/courses', tmp_path)
    with open(path_download_file) as file:
        expect_data = file.read()
    count_files = next(os.walk(get_path(
        '', tmp_path, 'ru-hexlet-io-courses_files')))[2]
    assert expect_data == correct_data
    assert len(count_files) == 2


def test_download3(tmp_path, requests_mock):
    for fixture in localhost_fixtures:
        with open(get_path(*fixture['path_file']), 'rb') as file:
            data = file.read()
            requests_mock.get(fixture['url'], content=data)
    with open(get_path('site-com-blog-about.html', 'expected')) as file:
        correct_data = file.read()
    with open(get_path('site-com-blog-about.html')) as file:
        initial_data = file.read()
        requests_mock.get('https://site.com/blog/about', text=initial_data)
        path_download_file = download('https://site.com/blog/about', tmp_path)
    with open(path_download_file) as file:
        expect_data = file.read()
    count_files = next(os.walk(get_path(
        '', tmp_path, 'site-com-blog-about_files')))[2]
    assert expect_data == correct_data
    assert len(count_files) == 4
