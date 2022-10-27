import re
from os.path import splitext
from urllib.parse import urlparse, urljoin


def get_name_from_url(path: str, url: str, dir: bool = False) -> str:
    parse_url = urlparse(urljoin(path, url))
    full_path = parse_url.netloc + parse_url.path
    name_file_without_extension = re.sub(r'\W', '-',
                                         splitext(full_path)[0])
    if dir is True:
        return f'{name_file_without_extension}_files'
    if splitext(full_path)[1]:
        return name_file_without_extension + splitext(full_path)[1]
    if not splitext(full_path)[1]:
        return f'{name_file_without_extension}.html'
