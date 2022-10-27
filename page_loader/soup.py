import requests
from bs4 import BeautifulSoup


def get_soup(path):
    response = requests.get(path)
    response.raise_for_status()
    return BeautifulSoup(response.content, 'html.parser')
