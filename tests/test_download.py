import tempfile
import pytest
import requests
from tests import get_path
from page_loader import download


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


def test_download(requests_mock):
    with tempfile.TemporaryDirectory() as tmp:
        url_1 = open(
            get_path('ru-hexlet-io-lessons.rss', 'ru-hexlet-io-courses_files'),
            'rb')
        data1 = url_1.read()
        requests_mock.get(
            'https://ru.hexlet.io/about/lessons.rss',
            content=data1)
        file_with_download = open(get_path('with_download.html'))
        correct_data = file_with_download.read()
        initial_file = open(get_path('initial.html'))
        initial_data = initial_file.read()
        requests_mock.get('https://ru.hexlet.io/courses', text=initial_data)
        path_download_file = download('https://ru.hexlet.io/courses', tmp)
        download_file = open(path_download_file)
        expect_data = download_file.read()
        assert expect_data == correct_data


def test_download2(requests_mock):
    with tempfile.TemporaryDirectory() as tmp:
        url_1 = open(get_path(
            'localhost-blog-about-assets-styles.css',
            'expected',
            'localhost-blog-about_files'),
            'rb')
        data1 = url_1.read()
        requests_mock.get(
            'https://localhost/blog/about/assets/styles.css',
            content=data1)
        url_2 = open(get_path(
            'localhost-blog-about.html',
            'expected',
            'localhost-blog-about_files'),
            'rb')
        data2 = url_2.read()
        requests_mock.get(
            'https://localhost/blog/about',
            content=data2)
        url_3 = open(get_path(
            'localhost-photos-me.jpg',
            'expected',
            'localhost-blog-about_files'),
            'rb')
        data3 = url_3.read()
        requests_mock.get(
            'https://localhost/photos/me.jpg',
            content=data3)
        url_4 = open(get_path(
            'localhost-assets-scripts.js',
            'expected',
            'localhost-blog-about_files'),
            'rb')
        data4 = url_4.read()
        requests_mock.get(
            'http://localhost/assets/scripts.js',
            content=data4)
        file_with_download = open(get_path(
            'localhost-blog-about.html',
            'expected'))
        correct_data = file_with_download.read()
        initial_file2 = open(get_path('localhost-blog-about.html'))
        initial_data2 = initial_file2.read()
        requests_mock.get('https://localhost/blog/about', text=initial_data2)
        path_download_file = download('https://localhost/blog/about', tmp)
        download_file = open(path_download_file)
        expect_data = download_file.read()
        assert expect_data == correct_data


def test_download3(requests_mock):
    with tempfile.TemporaryDirectory() as tmp:
        url_1 = open(get_path(
            'site-com-blog-about-assets-styles.css',
            'expected',
            'site-com-blog-about_files'),
            'rb')
        data1 = url_1.read()
        requests_mock.get(
            'https://site.com/blog/about/assets/styles.css',
            content=data1)
        url_2 = open(get_path(
            'site-com-blog-about.html',
            'expected',
            'site-com-blog-about_files'),
            'rb')
        data2 = url_2.read()
        requests_mock.get(
            'https://site.com/blog/about',
            content=data2)
        url_3 = open(get_path(
            'site-com-photos-me.jpg',
            'expected',
            'site-com-blog-about_files'),
            'rb')
        data3 = url_3.read()
        requests_mock.get(
            'https://site.com/photos/me.jpg',
            content=data3)
        url_4 = open(get_path(
            'site-com-assets-scripts.js',
            'expected',
            'site-com-blog-about_files'),
            'rb')
        data4 = url_4.read()
        requests_mock.get(
            'https://site.com/assets/scripts.js',
            content=data4)
        file_with_download = open(get_path(
            'site-com-blog-about.html',
            'expected'))
        correct_data = file_with_download.read()
        initial_file3 = open(get_path(
            'site-com-blog-about.html'))
        initial_data3 = initial_file3.read()
        requests_mock.get('https://site.com/blog/about', text=initial_data3)
        path_download_file = download('https://site.com/blog/about', tmp)
        download_file = open(path_download_file)
        expect_data = download_file.read()
        assert expect_data == correct_data
