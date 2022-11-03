import requests
from progress.bar import Bar
from page_loader.writing_file import write_data
import re
from os.path import splitext
from urllib.parse import urlparse, urljoin


def make_name_from_url(
        site_url: str,
        internal_url: str,
        is_dir: bool = False) -> str:
    parse_url = urlparse(urljoin(site_url, internal_url))
    full_path = parse_url.netloc + parse_url.path
    name_file_without_extension = re.sub(r'\W', '-',
                                         splitext(full_path)[0])
    if is_dir:
        return f'{name_file_without_extension}_files'
    if extension := splitext(full_path)[1]:
        return name_file_without_extension + extension
    if not extension:
        return f'{name_file_without_extension}.html'


def download_media_files(urls_and_paths: list[dict]):
    if urls_and_paths:
        for url_and_path in Bar('Processing').iter(urls_and_paths):
            response = requests.get(url_and_path.get('url'))
            response.raise_for_status()
            write_data(response.content, url_and_path.get('path'), 'wb')
