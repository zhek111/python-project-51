from page_loader.atrs import get_atr_and_url
from page_loader.domain import is_valid


def get_required_tags(site, required_tags):
    def inner(tag):
        if tag.name in required_tags:
            return is_valid(site, get_atr_and_url(tag).get('url'))
    return inner
