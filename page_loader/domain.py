from urllib.parse import urlparse


def check_domain(path1: str, path2: str) -> bool:
    if path2 is None:
        return False
    if not urlparse(path2).netloc:
        return True
    if urlparse(path2).netloc == urlparse(path1).netloc:
        return True
    return False
