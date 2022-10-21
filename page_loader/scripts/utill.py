#!/usr/bin/env python
import argparse
import os
import sys

from page_loader.page_loader import download


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
    try:
        print(download(args.URL, output_path=args.output))
    except BaseException:
        sys.exit(0)


if __name__ == '__main__':
    main()
