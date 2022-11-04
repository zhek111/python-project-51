import re
from os.path import splitext
from urllib.parse import urlparse, urljoin


def is_valid_domain(site_url: str, media_file_url: str) -> bool:
    if media_file_url is None:
        return False
    return not (netloc2 := urlparse(media_file_url).netloc) \
        or netloc2 == urlparse(site_url).netloc


def make_name_from_url(
        site_url: str,
        internal_url: str,
        is_dir: bool = False) -> str:
    parse_url = urlparse(urljoin(site_url, internal_url))
    full_path = parse_url.netloc + parse_url.path
    name_file_without_extension = re.sub(r'\W', '-', (
        divided_path := splitext(full_path))[0])
    if is_dir:
        return f'{name_file_without_extension}_files'
    if extension := divided_path[1]:
        return name_file_without_extension + extension
    if not extension:
        return f'{name_file_without_extension}.html'
