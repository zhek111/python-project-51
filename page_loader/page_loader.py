from pathlib import Path
import os
from page_loader.name_from_url import get_name_from_url
from page_loader.soup import get_soup
from page_loader.tags import tag_processing


def download(path: str, output_path: [str, Path] = os.getcwd()) -> str:
    if not os.path.isdir(output_path):
        raise FileNotFoundError
    full_path_page = os.path.join(output_path, get_name_from_url(path, path))
    soup = get_soup(path)
    tag_processing(soup, path, output_path, full_path_page)
    return full_path_page
