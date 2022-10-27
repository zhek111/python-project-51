import requests
import os
from urllib.parse import urljoin
from progress.bar import Bar
from page_loader.atrs import get_atrs
from page_loader.file_and_dir import make_dir_if_missing, safe_file
from page_loader.name_from_url import get_name_from_url
from page_loader.relevant_url import parent_relevant_url

TAGS = ['img', 'link', 'script']


def tag_processing(soup, path, output_path, full_path_page):
    nessasary_tags = soup.find_all(parent_relevant_url(path, TAGS))
    for link in Bar('Processing').iter(nessasary_tags):
        name_dir = os.path.join(output_path,
                                get_name_from_url(path, path, dir=True))
        url = get_atrs(link).get('url')
        make_dir_if_missing(name_dir)
        data = requests.get(urljoin(path, url))
        name_file = get_name_from_url(path, url)
        safe_file(data.content, os.path.join(name_dir, name_file), 'wb')
        link[get_atrs(link).get('atr')] = os.path.join(
            get_name_from_url(path, path, dir=True), name_file)
    safe_file(soup.prettify(), full_path_page, 'w+')
