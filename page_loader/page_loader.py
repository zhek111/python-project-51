import os
from pathlib import Path
from page_loader.html_processing import prepare_html_and_media_files
from page_loader.urls import download_media_files, make_name_from_url
from page_loader.writing_file import write_data


def download(site: str, output_path: [str, Path] = os.getcwd()) -> str:
    if not os.path.isdir(output_path):
        raise FileNotFoundError
    full_path_page = os.path.join(output_path, make_name_from_url(site, site))
    urls_and_paths, html_ = prepare_html_and_media_files(site,
                                                         output_path)
    write_data(html_, full_path_page, 'w+')
    download_media_files(urls_and_paths)
    return full_path_page
