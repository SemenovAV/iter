import json
import requests
with open('countries.json','r', encoding='utf8') as f:
    s = json.load(f)
    for item in s:
        S = requests.Session()

        URL = "https://en.wikipedia.org/w/api.php"

        SEARCHPAGE = item['name']['common']

        PARAMS = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": SEARCHPAGE
        }

        R = S.get(url=URL, params=PARAMS)
        DATA = R.json()
        pageid = DATA['query']['search'][0]['pageid']
        print(pageid)
        PARAMS2 = {
            "action": "query",
            "format": "json",
            "inprop": "url",
            "prop": "info",
            "pageids": [pageid],
        }
        r2 = S.get(url=URL, params=PARAMS2)
        DATA2 = r2.json()
        if DATA2:
            print(DATA2['query']['pages'][f'{pageid}']['canonicalurl'])