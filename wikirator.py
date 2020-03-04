import json
import requests
import wikipedia_api.api as api


class GetUrl:
    def __init__(self, filepath):
        with open(filepath, encoding='utf8') as f:
            countries = json.load(f)
            session = requests.Session()
            for item in countries:
                search_page = item['name']['common']
                print(api.get_url(api.get_ids(search_page, session), session))
            session.close()
