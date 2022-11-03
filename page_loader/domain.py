from urllib.parse import urlparse


def is_valid(site_url: str, media_file_url: str) -> bool:
    if media_file_url is None:
        return False
    return not (netloc2 := urlparse(media_file_url).netloc) \
        or netloc2 == urlparse(site_url).netloc
