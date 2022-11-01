import requests
import os
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from page_loader.atrs import get_atr_and_url
from page_loader.name_from_url import make_name_from_url
from page_loader.relevant_url import get_required_tags

TAGS = ['img', 'link', 'script']


def change_html_and_get_urls_for_download(url: str) -> (list[str], str):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    nessasary_tags = soup.find_all(get_required_tags(url, TAGS))
    urls = list()
    for tag in nessasary_tags:
        urls.append(
            internal_url := urljoin(url, get_atr_and_url(tag).get('url')))
        name_file = make_name_from_url(url, internal_url)
        tag[get_atr_and_url(tag).get('atr')] = os.path.join(
            make_name_from_url(url, url, is_dir=True), name_file)
    return urls, soup.prettify()
