import os
import requests
from pathlib import Path
from page_loader.html_processing import change_html_and_get_urls_for_download
from page_loader.name_from_url import make_name_from_url
from page_loader.urls import download_urls


def download(site: str, output_path: [str, Path] = os.getcwd()) -> str:
    if not os.path.isdir(output_path):
        raise FileNotFoundError
    full_path_page = os.path.join(output_path, make_name_from_url(site, site))
    response = requests.get(site)
    response.raise_for_status()
    urls, html_ = change_html_and_get_urls_for_download(site)
    download_urls(urls, site, output_path, html_, full_path_page)
    return full_path_page
