

URL = "https://en.wikipedia.org/w/api.php"


def get_ids(data, session):
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": data
    }

    res = session.get(url=URL, params=params)
    search_data = res.json()
    return search_data['query']['search'][0]['pageid']


def get_url(wiki_page_id, session):
    params = {
        "action": "query",
        "format": "json",
        "inprop": "url",
        "prop": "info",
        "pageids": [wiki_page_id],
    }
    res = session.get(url=URL, params=params)
    data = res.json()
    if data:
        return data['query']['pages'][f'{wiki_page_id}']['canonicalurl']