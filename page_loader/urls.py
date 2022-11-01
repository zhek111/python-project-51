import requests
import os
from pathlib import Path
from progress.bar import Bar
from page_loader.writing_file import write_data
from page_loader.name_from_url import make_name_from_url


def download_urls(urls: list, site: str, output_path: [str, Path], html: str,
                  full_path_page: str):
    if urls:
        name_dir = os.path.join(output_path,
                                make_name_from_url(site, site, is_dir=True))
        if not os.path.isdir(name_dir):
            os.mkdir(name_dir)
        for internal_url in Bar('Processing').iter(urls):
            response = requests.get(internal_url)
            response.raise_for_status()
            name_file = make_name_from_url(site, internal_url)
            write_data(response.content, os.path.join(name_dir, name_file),
                       'wb')
    write_data(html, full_path_page, 'w+')
