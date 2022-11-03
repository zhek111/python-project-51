import os


def get_fixture_path(*path):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures',
                        *path)


def read_file(path, mode='r'):
    with open(path, mode) as file:
        return file.read()
