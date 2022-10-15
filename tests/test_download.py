import tempfile
from logic.page_loader import download


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
