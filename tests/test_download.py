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
    with pytest.raises(ConnectionError):
        requests_mock.get('https://ru.hexlettt.io/courses',
                          exc=requests.RequestException)
        download('https://ru.hexlettt.io/courses')


def test_download(requests_mock):
    file_with_download = open('tests/fixtures/with_download.html')
    correct_data = file_with_download.read()
    with tempfile.TemporaryDirectory() as tmp:
        url_1 = open(
            'tests/fixtures/ru-hexlet-io-courses_files/'
            'ru-hexlet-io-lessons.rss', 'rb')
        data1 = url_1.read()
        requests_mock.get(
            'https://ru.hexlet.io/lessons.rss',
            content=data1)

        initial_file = open('tests/fixtures/initial.html')
        initial_data = initial_file.read()
        requests_mock.get('https://ru.hexlet.io/courses', text=initial_data)

        path_download_file = download('https://ru.hexlet.io/courses', tmp)
        download_file = open(path_download_file)
        expect_data = download_file.read()

        assert expect_data == correct_data
