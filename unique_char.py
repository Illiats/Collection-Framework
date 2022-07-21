import collections
from functools import lru_cache


@lru_cache(maxsize=10)
def unique_chars(string):
    if type(string) != str:
        raise TypeError
    counter = collections.Counter(string)
    non_repeated = {}
    for key, value in counter.items():
        if value == 1:
            non_repeated[key] = value

    return len(non_repeated)
