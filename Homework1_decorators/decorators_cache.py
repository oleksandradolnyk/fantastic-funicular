import functools
from collections import OrderedDict
import requests

def cache(max_limit=1):
    try:
        max_limit = int(max_limit)
    except ValueError as e:
        print(e)
        exit(1)
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))
            if cache_key in deco._cache:
                deco._cache_counts[cache_key] += 1
                return deco._cache[cache_key]
            result = f(*args, **kwargs)
            if len(deco._cache) >= max_limit:
                lowest = min(deco._cache_counts, key=deco._cache_counts.get)
                print('lowest:', lowest)
                del deco._cache[lowest]
                del deco._cache_counts[lowest]
            deco._cache[cache_key] = result
            deco._cache_counts[cache_key] = 1
            return result
        deco._cache = OrderedDict()
        deco._cache_counts = {}
        return deco
    return internal

@cache(max_limit=input("Max cache limit:"))
def fetch_url(url, first_n=50):
    """Fetch a given url"""
    res = requests.get(url)
    # print(res)
    return res.content[:first_n] if first_n else res.content


fetch_url('https://google.com')
fetch_url('https://google.com')
fetch_url('https://www.linkedin.com')
fetch_url('https://ithillel.ua')
fetch_url('https://ithillel.ua')
fetch_url('https://refactoring.guru')
fetch_url('https://open.spotify.com')
fetch_url('https://youtube.com')
fetch_url('https://youtube.com')
fetch_url('https://youtube.com')
fetch_url('https://youtube.com')
fetch_url('https://open.spotify.com')






