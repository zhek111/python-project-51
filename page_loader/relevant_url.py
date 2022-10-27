from page_loader.atrs import get_atrs
from page_loader.domain import is_valid


def parent_relevant_url(current_path, acceptible_tags):
    def has_relavant_url(tag):
        if tag.name in acceptible_tags:
            return is_valid(current_path, get_atrs(tag).get('url'))
    return has_relavant_url
