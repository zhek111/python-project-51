import os
import tempfile

import pytest
import requests

from page_loader import download


def test_error_download(requests_mock):
    with pytest.raises(OSError):
        initial_file = open('tests/fixtures/initial.html')
        initial_data = initial_file.read()
        requests_mock.get('https://ru.hexlet.io/courses', text=initial_data)
        download('https://ru.hexlet.io/courses', '/undefined')


def test_error_download2(requests_mock):
    with pytest.raises(Exception):
        requests_mock.get('https://ru.hexlettt.io/courses',
                          exc=requests.RequestException)
        download('https://ru.hexlettt.io/courses')


# def test_download(requests_mock):
#     file_with_download = open('tests/fixtures/with_download.html')
#     correct_data = file_with_download.read()
#     with tempfile.TemporaryDirectory() as tmp:
#         url_1 = open(
#             'tests/fixtures/ru-hexlet-io-courses_files/'
#             'ru-hexlet-io-lessons.rss', 'rb')
#         data1 = url_1.read()
#         requests_mock.get(
#             'https://ru.hexlet.io/about/lessons.rss',
#             content=data1)
#         initial_file = open('tests/fixtures/initial.html')
#         initial_data = initial_file.read()
#         requests_mock.get('https://ru.hexlet.io/courses', text=initial_data)
#         path_download_file = download('https://ru.hexlet.io/courses', tmp)
#         download_file = open(path_download_file)
#         expect_data = download_file.read()
#         assert expect_data == correct_data

# def test_download2(requests_mock):
#     with tempfile.TemporaryDirectory() as tmp:
#         url_1 = open(
#             'tests/fixtures/expected/localhost-blog-about_files/localhost'
#             '-blog-about-assets-styles.css',
#             'rb')
#         data1 = url_1.read()
#         requests_mock.get(
#             'https://localhost/blog/about/assets/styles.css',
#             content=data1)
# 
#         url_2 = open(
#             'tests/fixtures/expected/localhost-blog-about_files/localhost'
#             '-blog-about.html',
#             'rb')
#         data2 = url_2.read()
#         requests_mock.get(
#             'https://localhost/blog/about',
#             content=data2)
# 
#         url_3 = open(
#             'tests/fixtures/expected/localhost-blog-about_files/localhost'
#             '-photos-me.jpg',
#             'rb')
#         data3 = url_3.read()
#         requests_mock.get(
#             'https://localhost/photos/me.jpg',
#             content=data3)
# 
#         url_4 = open(
#             'tests/fixtures/expected/localhost-blog-about_files/localhost'
#             '-assets-scripts.js',
#             'rb')
#         data4 = url_4.read()
#         requests_mock.get(
#             'http://localhost/assets/scripts.js',
#             content=data4)
#         file_with_download = open(
#             'tests/fixtures/expected/localhost'
#             '-blog-about.html')
#         correct_data = file_with_download.read()
#         initial_file2 = open('tests/fixtures/localhost-blog-about.html')
#         initial_data2 = initial_file2.read()
#         requests_mock.get('https://localhost/blog/about', text=initial_data2)
# 
#         path_download_file = download('https://localhost/blog/about', tmp)
#         download_file = open(path_download_file)
#         expect_data = download_file.read()
# 
#         assert expect_data == correct_data

def test_download3(requests_mock):
    with tempfile.TemporaryDirectory() as tmp:
        url_1 = open(
            'tests/fixtures/expected/site-com-blog-about_files/site-com-blog-about-assets-styles.css',
            'rb')
        data1 = url_1.read()
        requests_mock.get(
            'https://site.com/blog/about/assets/styles.css',
            content=data1)

        url_2 = open(
            'tests/fixtures/expected/site-com-blog-about_files/site-com-blog-about.html',
            'rb')
        data2 = url_2.read()
        requests_mock.get(
            'https://site.com/blog/about',
            content=data2)

        url_3 = open(
            'tests/fixtures/expected/site-com-blog-about_files/site-com-photos-me.jpg',
            'rb')
        data3 = url_3.read()
        requests_mock.get(
            'https://site.com/photos/me.jpg',
            content=data3)

        url_4 = open(
            'tests/fixtures/expected/site-com-blog-about_files/site-com-assets-scripts.js',
            'rb')
        data4 = url_4.read()
        requests_mock.get(
            'https://site.com/assets/scripts.js',
            content=data4)
        file_with_download = open(
            'tests/fixtures/expected/site-com-blog-about.html')
        correct_data = file_with_download.read()
        initial_file3 = open('tests/fixtures/site-com-blog-about.html')
        initial_data3 = initial_file3.read()
        requests_mock.get('https://site.com/blog/about', text=initial_data3)

        path_download_file = download('https://site.com/blog/about', tmp)
        download_file = open(path_download_file)
        expect_data = download_file.read()

        assert expect_data == correct_data