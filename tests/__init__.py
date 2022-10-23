import os


def get_path(file, *dir):
    return os.path.join('tests', 'fixtures', *dir, file)
