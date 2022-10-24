import requests
import re
from os.path import splitext
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import logging

from progress.bar import Bar
from requests import HTTPError

logging.basicConfig(level=logging.DEBUG)


def get_name_data(path, url, dir=None):
    aaa = urlparse(urljoin(path, url))
    logging.debug(aaa)
    full_path = aaa.netloc + aaa.path + aaa.params + aaa.query + aaa.fragment
    logging.debug(full_path)
    name_file_without_extension = re.sub(r'\W', '-',
                                         splitext(full_path)[0])
    logging.debug(name_file_without_extension)
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
        return {'url': link['src'], 'atr': 'src'}
    if link.get('href'):
        return {'url': link['href'], 'atr': 'href'}
    return {'url': None, 'atr': None}


def download(path, output_path=os.getcwd()):
    try:
        os.chdir(output_path)
    except OSError as e:
        logging.error(e)
        print('Такая директория не существует')
        raise
    try:
        requests.get(path)
    except requests.RequestException as e:
        logging.error(e)
        print('Введите другой сайт!!!!AAAAAAAAAA')
        raise
    try:
        r = requests.get(path)
        r.raise_for_status()
    except HTTPError as e:
        logging.error(e)
        print('AAA')
        logging.debug('GGGGGGGTTTGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG')
        raise
    full_path_page = os.path.join(output_path, get_name_data(path, path))
    logging.debug(full_path_page)
    name_dir = os.path.join(output_path, get_name_data(path, path, dir=True))
    logging.debug(name_dir)
    response = requests.get(path)
    soup = BeautifulSoup(response.content, 'html.parser')
    nessasary_tags = soup.find_all(['img', 'link', 'script'])
    necessary_urls = []
    for teg in nessasary_tags:
        atrs = get_atrs(teg)
        if check_domain(path, atrs.get('url')):
            necessary_urls.append(atrs)
            logging.debug(atrs)
    for link in nessasary_tags:
        url = get_atrs(link).get('url')
        logging.debug(url)
        if check_domain(path, url):
            if not os.path.isdir(name_dir):
                logging.debug(name_dir)
                os.mkdir(name_dir)
            for i in Bar('Processing').iter(necessary_urls):
                data = requests.get(urljoin(path, url))
            name_file = get_name_data(path, url)
            print('NAME FILE', name_file)
            print('NAME DIR', name_dir)
            with open(os.path.join(name_dir, name_file), 'wb') as file:
                file.write(data.content)
            link[get_atrs(link).get('atr')] = os.path.join(
                get_name_data(path, path, dir=True), name_file)
    with open(full_path_page, 'w+') as file:
        file.write(soup.prettify())
    return full_path_page
