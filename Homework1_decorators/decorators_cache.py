import functools, psutil, requests
from collections import OrderedDict

def cache(max_limit=64):
    try:
        max_limit = int(max_limit)
    except ValueError as e:
        print(e)
        exit(1)
    if max_limit <= 0:
        print("Cache limit can not be 0 or less.")
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

def process_memory(f):
    @functools.wraps(f)
    def internal(*args, **kwargs):
        process = psutil.Process()
        f(*args, **kwargs)
        mem = process.memory_info().rss / (1024 ** 2)
        print("Used memory: ", mem)
        return mem
    return internal

@cache(max_limit=input("Max cache limit: "))
@process_memory
def fetch_url(url, first_n=50):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content

fetch_url("https://google.com")
fetch_url("https://stackoverflow.com/")
fetch_url("https://google.com")