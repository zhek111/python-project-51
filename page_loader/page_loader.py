import requests
import re
from os.path import splitext
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import logging

from progress.bar import Bar

logging.basicConfig(level='DEBUG')


def get_name_data(path, url, dir=None):
    full_path = urljoin(path, url)
    name_file_without_extension = re.sub(r'\W', '-',
                                         splitext(full_path)[0][8:])
    if dir:
        return f'{name_file_without_extension}_files'
    if splitext(full_path)[1]:
        return name_file_without_extension + splitext(full_path)[1]
    if not splitext(full_path)[1]:
        return f'{name_file_without_extension}.html'


def check_domain(path1, path2):
    if path2 is None:
        return False
    if not urlparse(path2).netloc:
        return True
    if urlparse(path2).netloc == urlparse(path1).netloc:
        return True
    return False


def get_atrs(link):
    if link.get('src'):
        return {'url': link['src'], 'atr': 'srs'}
    if link.get('href'):
        return {'url': link['href'], 'atr': 'href'}
    return {'url': None, 'atr': None}


def download(path, output_path=os.getcwd()):
    if not os.path.isdir(output_path):
        raise OSError('Такая директория не существует')
    try:
        requests.get(path)
    except requests.RequestException:
        raise ConnectionError('Введите другой сайт')
    try:
        r = requests.get(path)
        r.raise_for_status()
    except requests.RequestException:
        raise ConnectionError('AAA')
    full_path_page = os.path.join(output_path, get_name_data(path, path))
    name_dir = os.path.join(output_path, get_name_data(path, path, dir=True))
    response = requests.get(path)
    soup = BeautifulSoup(response.content, 'html.parser')
    nessasary_tags = soup.find_all(['img', 'link', 'script'])
    necessary_urls = []
    for teg in nessasary_tags:
        atrs = get_atrs(teg)
        if check_domain(path, atrs.get('url')):
            necessary_urls.append(atrs)
    for link in nessasary_tags:
        url = get_atrs(link).get('url')
        if check_domain(path, url):
            if not os.path.isdir(name_dir):
                os.mkdir(name_dir)
            os.chdir(name_dir)
            for i in Bar('Processing').iter(necessary_urls):
                data = requests.get(urljoin(path, url))
            name_file = get_name_data(path, url)
            with open(name_file, 'wb') as file:
                file.write(data.content)
            link[get_atrs(link).get('atr')] = os.path.join(
                get_name_data(path, path, dir=True), name_file)
    with open(full_path_page, 'w+') as file:
        file.write(soup.prettify())
    return full_path_page
