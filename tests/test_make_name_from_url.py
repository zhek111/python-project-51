import pytest
from page_loader.urls import make_name_from_url


@pytest.mark.parametrize(
    "site_url, internal_url, is_dir, result",
    [
        pytest.param(
            'https://ru.hexlet.io/courses',
            'https://ru.hexlet.io/courses',
            True,
            'ru-hexlet-io-courses_files',
            id="test_dir"
        ),
        pytest.param(
            'https://ru.hexlet.io/courses',
            'https://ru.hexlet.io/courses',
            False,
            'ru-hexlet-io-courses.html',
            id="test_html"
        ),
        pytest.param(
            'https://ru.hexlet.io/courses',
            '/assets/menu',
            False,
            'ru-hexlet-io-assets-menu.html',
            id="test_local_path"
        )
    ]
)
def test_make_name_from_url(site_url, internal_url, is_dir, result):
    assert make_name_from_url(site_url, internal_url, is_dir) == result
