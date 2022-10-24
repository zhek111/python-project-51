#!/usr/bin/env python
import argparse
import logging
import os
import sys

from page_loader.page_loader import download

logging.basicConfig(level=logging.DEBUG)


def main():
    try:
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
    except Exception as e:
        logging.error(e)
        print('XN')
        sys.exit(1)


if __name__ == '__main__':
    main()
