import tempfile
from logic.page_loader import download


def test_download(requests_mock):
    with tempfile.TemporaryDirectory() as tmp:
        file = open('tests/fixtures/ru-hexlet-io-courses.html')
        correct_data = file.read()
        requests_mock.get('https://ru.hexlet.io/courses', text=correct_data)
        path_download_file = download('https://ru.hexlet.io/courses', tmp)
        download_file = open(path_download_file)
        data_download_file = download_file.read()
        assert data_download_file == correct_data
