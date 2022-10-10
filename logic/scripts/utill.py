#!/usr/bin/env python
import argparse
import os

from logic.page_loader import download


def main():
    parser = argparse.ArgumentParser(
        description='downloads page from the network and puts it in the '
                    'specified existing directory'
    )
    parser.add_argument('URL')
    parser.add_argument('-o', '--output',
                        default=os.getcwd(),
                        help='set path output')
    args = parser.parse_args()
    print(download(args.URL, output_path=args.output))


if __name__ == '__main__':
    main()
