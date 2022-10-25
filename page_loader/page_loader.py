import requests
import os
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from progress.bar import Bar
from page_loader.atrs import get_atrs
from page_loader.domain import check_domain
from page_loader.name_data import get_name_data


def download(path: str, output_path: str = os.getcwd()) -> str:
    if not os.path.isdir(output_path):
        raise FileNotFoundError
    full_path_page = os.path.join(output_path, get_name_data(path, path))
    response = requests.get(path)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    nessasary_tags = soup.find_all(['img', 'link', 'script'])
    # тут хотелось бы сделать функцию, которую можно положить в
    # soup.find_all(),
    # чтобы искать сразу нужные теги. Но у меня не получается.
    necessary_tegs2 = []
    for teg in nessasary_tags:
        atrs = get_atrs(teg)
        if check_domain(path, atrs.get('url')):
            necessary_tegs2.append(teg)
    for link in Bar('Processing').iter(necessary_tegs2):
        name_dir = os.path.join(output_path,
                                get_name_data(path, path, dir=True))
        url = get_atrs(link).get('url')
        if not os.path.isdir(name_dir):
            os.mkdir(name_dir)
        data = requests.get(urljoin(path, url))
        name_file = get_name_data(path, url)
        with open(os.path.join(name_dir, name_file), 'wb') as file:
            file.write(data.content)
        link[get_atrs(link).get('atr')] = os.path.join(
            get_name_data(path, path, dir=True), name_file)

    with open(full_path_page, 'w+') as file:
        file.write(soup.prettify())
    return full_path_page
