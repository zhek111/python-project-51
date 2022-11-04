import os
import requests
from pathlib import Path
from progress.bar import Bar
from page_loader.html_processing import prepare_html_and_media_files
from page_loader.urls import make_name_from_url
from page_loader.file import write_data_to_file


def download_media_files(urls_and_paths: list[dict]):
    if urls_and_paths:
        for url_and_path in Bar('Processing').iter(urls_and_paths):
            response = requests.get(url_and_path.get('url'))
            response.raise_for_status()
            write_data_to_file(response.content, url_and_path.get('path'),
                               'wb')


def download(site: str, output_path: [str, Path] = os.getcwd()) -> str:
    if not os.path.isdir(output_path):
        raise FileNotFoundError
    full_path_page = os.path.join(output_path, make_name_from_url(site, site))
    urls_and_paths, file_full_path = prepare_html_and_media_files(site,
                                                                  output_path)
    download_media_files(urls_and_paths)
    write_data_to_file(file_full_path, full_path_page, 'w+')
    return full_path_page
