import functools, psutil, requests
from collections import OrderedDict

def cache(max_limit: int = 64):
    """max_limit argument must be an integer"""
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
                deco._cache.pop(lowest)
                deco._cache_counts.pop(lowest)
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
        result = f(*args, **kwargs)
        used_memory = process.memory_info().rss / (1024 ** 2)
        print("Used memory: ", used_memory)
        return result
    return internal

@cache(max_limit=int(input("Max cache limit: ")))
@process_memory
def fetch_url(url, first_n=50):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content

fetch_url("https://google.com")
fetch_url("https://stackoverflow.com/")
fetch_url("https://google.com")