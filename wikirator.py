import json

import requests

import wikipedia_api.api as api


class Wikirator:
    def __init__(self, filepath, result_filepath, end=20):
        with open(filepath, encoding='utf8') as f:
            self.countries = [item['name']['common'] for item in json.load(f)]
            self.start = -1
            self.end = end or len(self.countries)
            self.session = requests.Session()
            self.result_filepath = result_filepath

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        result = f'{self.countries[self.start]} - {api.get_url(api.get_ids(self.countries[self.start], self.session), self.session)}'
        with open(self.result_filepath, 'a', encoding='utf8') as res:
            res.write(f'{result}\n')
        return result

    def __del__(self):
        self.session.close()
