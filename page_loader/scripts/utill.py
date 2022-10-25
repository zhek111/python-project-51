#!/usr/bin/env python
import logging
import sys
import requests
from page_loader.cli import parse
from page_loader.page_loader import download

logging.basicConfig(level=logging.ERROR)


def main():
    try:
        args = parse()
        print(download(args.URL, output_path=args.output))

    except requests.exceptions.HTTPError:
        logging.error('This page was not found')
        sys.exit(1)
    except requests.exceptions.ConnectionError:
        logging.error('Connection error')
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        logging.error('Other connection error')
        logging.error(e)
        sys.exit(1)
    except FileNotFoundError:
        logging.error('The specified directory does not exist or is a file')
        sys.exit(1)
    except Exception as e:
        logging.error(e)
        logging.error('Error')
        sys.exit(1)


if __name__ == '__main__':
    main()
