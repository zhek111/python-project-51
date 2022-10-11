import tempfile
from logic.page_loader import download


def test_download(requests_mock):
    file_with_download = open('tests/fixtures/with_download.html')
    correct_data = file_with_download.read()
    with tempfile.TemporaryDirectory() as tmp:
        image1_file = open(
            'tests/fixtures/ru-hexlet-io-courses_files/cdn2-hexlet-io-assets'
            '-logo_ru-495f05850e0095ea722a2b583565d492719579'
            'c02b0ce61d924e4f895fabf781.svg',
            'rb')
        image1 = image1_file.read()
        requests_mock.get(
            'https://cdn2.hexlet.io/assets/logo_ru'
            '-495f05850e0095ea722a2b583565d492719'
            '579c02b0ce61d924e4f895fabf781.svg',
            content=image1)

        image2_file = open(
            'tests/fixtures/ru-hexlet-io-courses_files/cdn2-hexlet-io-assets-'
            'at_a_laptop-8c6e59267f91a6bf13bae0e5c0f7e1f36a'
            'ccc440b8d760bca08ab244e2b8bdbf.png',
            'rb')
        image2 = image2_file.read()
        requests_mock.get(
            'https://cdn2.hexlet.io/assets/at_a_laptop-8c6e59267f91a6bf13bae0e'
            '5c0f7e1f36accc440b8d760bca08ab244e2b8bdbf.png',
            content=image2)

        image3_file = open(
            'tests/fixtures/ru-hexlet-io-courses_files/cdn2-hexlet-io-assets'
            '-fl'
            'ag-en-f0b48c6562bb27879fbd685ece0133271ea04'
            '3384dd9793843c246f862ac7cc1.svg',
            'rb')
        image3 = image3_file.read()
        requests_mock.get(
            'https://cdn2.hexlet.io/assets/flag-en-f0b48c6562bb27879fbd685ece0'
            '133271ea043384dd9793843c246f862ac7cc1.svg',
            content=image3)

        image4_file = open(
            'tests/fixtures/ru-hexlet-io-courses_files/cdn2-hexlet-io-ass'
            'ets-flag-ru-593864ce87ae202b2c2e9393b2a6cf9384ac9cbb1c70632f'
            '4c6eeca34341483e.svg',
            'rb')
        image4 = image4_file.read()
        requests_mock.get(
            'https://cdn2.hexlet.io/assets/flag-ru-593864ce87ae202b2c2e9393b2a'
            '6cf9384ac9cbb1c70632f4c6eeca34341483e.svg',
            content=image4)

        initial_file = open('tests/fixtures/initial.html')
        initial_data = initial_file.read()
        requests_mock.get('https://ru.hexlet.io/courses', text=initial_data)

        path_download_file = download('https://ru.hexlet.io/courses', tmp)
        download_file = open(path_download_file)
        expect_data = download_file.read()

        assert expect_data == correct_data
