import os


def get_fixture_path(*path):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures',
                        *path)


def read_file(file, type='r'):
    with open(file, type) as file:
        return file.read()
