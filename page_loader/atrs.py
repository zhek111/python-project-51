def get_atr_and_url(tag: dict) -> dict[str]:
    if tag.get('src'):
        return {'url': tag['src'], 'atr': 'src'}
    if tag.get('href'):
        return {'url': tag['href'], 'atr': 'href'}
    return {'url': None, 'atr': None}
