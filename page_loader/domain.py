from urllib.parse import urlparse


def is_valid(url1: str, url2: str) -> bool:
    if url2 is None:
        return False
    return not (netloc2 := urlparse(url2).netloc
                ) or netloc2 == urlparse(url1).netloc
