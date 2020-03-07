import json

import requests

import wikipedia_api.api as api


class GetUrl:
    def __init__(self, filepath):
        with open(filepath, encoding='utf8') as f:
            self.countries = [item['name']['common'] for item in json.load(f)]
            self.start = -1
            self.end = len(self.countries)
            self.session = requests.Session()
            self.session.close()

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        return api.get_url(api.get_ids(self.countries[self.start], self.session), self.session)
