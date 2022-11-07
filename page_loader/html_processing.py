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
        media_files_dir_full_path = os.path.join(
            output_path,
            name_dir := make_name_from_url(url, url, is_dir=True)
        )
        if not os.path.isdir(media_files_dir_full_path):
            os.mkdir(media_files_dir_full_path)
        for tag in nessasary_tags:
            media_file_url = urljoin(url, tag.get(TAGS[tag.name]))
            name_file = make_name_from_url(url, media_file_url)
            tag[TAGS[tag.name]] = os.path.join(name_dir, name_file)
            file_full_path = os.path.join(media_files_dir_full_path, name_file)
            media_files_urls_and_path.append(
                {
                    'url': media_file_url,
                    'path': file_full_path
                }
            )
    return media_files_urls_and_path, soup.prettify()
