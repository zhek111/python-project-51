import requests
import os
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from page_loader.relevant_url import get_valid_tags, TAGS
from page_loader.urls import make_name_from_url


def prepare_html_and_media_files(url: str, output_path: str) -> (
        list[dict], str):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    nessasary_tags = soup.find_all(get_valid_tags(url, TAGS))
    media_files_urls_and_path = list()
    if nessasary_tags:
        name_dir = os.path.join(output_path,
                                make_name_from_url(url, url, is_dir=True))
        if not os.path.isdir(name_dir):
            os.mkdir(name_dir)
        for tag in nessasary_tags:
            media_file_url = urljoin(url, tag.get(TAGS[tag.name]))
            name_file = make_name_from_url(url, media_file_url)
            tag[TAGS[tag.name]] = os.path.join(
                make_name_from_url(url, url, is_dir=True), name_file)
            path_ = os.path.join(name_dir, name_file)
            media_files_urls_and_path.append(
                {
                    'url': media_file_url,
                    'path': path_
                }
            )
    return media_files_urls_and_path, soup.prettify()
