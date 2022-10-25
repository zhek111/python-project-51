import argparse
import os


def parse():
    parser = argparse.ArgumentParser(
        description='downloads page from the network and puts it in the '
                    'specified existing directory'
    )
    parser.add_argument('URL')
    parser.add_argument('-o', '--output',
                        default=os.getcwd(),
                        help='set path output')
    return parser.parse_args()
