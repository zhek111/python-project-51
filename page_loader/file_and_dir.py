import os


def safe_file(data, file, type):
    with open(file, type) as file:
        file.write(data)


def make_dir_if_missing(dir):
    if not os.path.isdir(dir):
        os.mkdir(dir)
