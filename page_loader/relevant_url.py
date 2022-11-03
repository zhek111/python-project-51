import bs4

from page_loader.domain import is_valid

TAGS = {
    'img': 'src',
    'link': 'href',
    'script': 'src'
}


def get_valid_tags(site: str, required_tags: dict):
    def inner(tag: bs4) -> bool:
        if tag.name in required_tags:
            return is_valid(site, tag.get(TAGS[tag.name]))
    return inner
