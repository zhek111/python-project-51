from urllib.parse import urljoin

import requests
import re
from os.path import splitext
import os

from bs4 import BeautifulSoup


def download(path, output_path=os.getcwd()):
    name_url = re.sub(r'\W', '-', splitext(path)[0][8:])
    full_name = f"{output_path}/{name_url}.html"
    response = requests.get(path)
    name_dir = f"{output_path}/{name_url}_files"
    if not os.path.isdir(name_dir):
        os.mkdir(name_dir)
    os.chdir(name_dir)
    soup = BeautifulSoup(response.content, 'html.parser')
    for link in soup.find_all('img'):
        image = requests.get(link['src'])
        full_url = urljoin(path, link['src'])
        name_image = re.sub(r'\W', '-', splitext(full_url)[0][8:]) + \
            splitext(full_url)[1]
        with open(name_image, 'wb') as file:
            file.write(image.content)
        link['src'] = f'{name_url}_files/{name_image}'
    with open(full_name, 'w+') as file:
        file.write(soup.prettify())
    with open('AAA', 'wb') as file:
        file.write(response.content)
    return full_name
