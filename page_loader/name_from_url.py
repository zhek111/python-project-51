import re
from os.path import splitext
from urllib.parse import urlparse, urljoin


def make_name_from_url(url1: str, url2: str, is_dir: bool = False) -> str:
    parse_url = urlparse(urljoin(url1, url2))
    full_path = parse_url.netloc + parse_url.path
    name_file_without_extension = re.sub(r'\W', '-',
                                         splitext(full_path)[0])
    if is_dir is True:
        return f'{name_file_without_extension}_files'
    if splitext(full_path)[1]:
        return name_file_without_extension + splitext(full_path)[1]
    if not splitext(full_path)[1]:
        return f'{name_file_without_extension}.html'
