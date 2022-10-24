import os


def get_path(file, *dir):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures',
                        *dir, file)
