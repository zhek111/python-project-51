def get_atrs(link: dict) -> dict[str]:
    if link.get('src'):
        return {'url': link['src'], 'atr': 'src'}
    if link.get('href'):
        return {'url': link['href'], 'atr': 'href'}
    return {'url': None, 'atr': None}
