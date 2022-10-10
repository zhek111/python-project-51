import requests
import re
from os.path import splitext
import os


def download(path, output_path=os.getcwd()):
    name_url = re.sub(r'\W', '-', splitext(path)[0][8:])
    full_name_path = f"{output_path}/{name_url}.html"
    response = requests.get(path)
    with open(full_name_path, 'w+') as file:
        file.write(response.text)
    return full_name_path
