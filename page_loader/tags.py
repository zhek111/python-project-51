import requests
import os
from urllib.parse import urljoin
from progress.bar import Bar
from page_loader.atrs import get_atr_and_url
from page_loader.html_processing import TAGS
from page_loader.writing_file import write_data
from page_loader.name_from_url import make_name_from_url
from page_loader.relevant_url import get_required_tags


def tag_processing(soup, path, output_path, full_path_page):
    nessasary_tags = soup.find_all(get_required_tags(path, TAGS))
    name_dir = os.path.join(output_path,
                            make_name_from_url(path, path, is_dir=True))
    if nessasary_tags:
        if not os.path.isdir(name_dir):
            os.mkdir(name_dir)
    for link in Bar('Processing').iter(nessasary_tags):
        url = get_atr_and_url(link).get('url')
        data = requests.get(urljoin(path, url))
        name_file = make_name_from_url(path, url)
        write_data(data.content, os.path.join(name_dir, name_file), 'wb')
        link[get_atr_and_url(link).get('atr')] = os.path.join(
            make_name_from_url(path, path, is_dir=True), name_file)
    write_data(soup.prettify(), full_path_page, 'w+')
