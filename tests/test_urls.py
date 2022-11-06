import pytest
from page_loader.urls import make_name_from_url, is_valid_domain


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


@pytest.mark.parametrize(
    "site_url, media_file_url, result",
    [
        pytest.param(
            'https://ru.hexlet.io/courses',
            '/courses',
            True,
            id="test_local"
        ),
        pytest.param(
            'https://ru.hexlet.io/courses',
            'https://ru.hexlet.io/courses',
            True,
            id="test_full"
        ),
        pytest.param(
            'https://ru.hexlet.io/courses',
            'https://cdn2.hexlet.io/courses',
            False,
            id="test_other_domain"
        ),
        pytest.param(
            'https://ru.hexlet.io/courses',
            'https://site.com',
            False,
            id="test_other_site"
        )
    ]
)
def test_is_valid_domain(site_url, media_file_url, result):
    assert is_valid_domain(site_url, media_file_url) == result
