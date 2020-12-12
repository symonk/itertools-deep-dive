from itertools import count
from sys import getsizeof
from typing import Generator

"""
Arguments:
    start: `int`, default = 0
    step: `int`, default = 1
    
Given a starting point & a step, create a memory efficient iterator incrementing start by step indefinitely.
"""


def count_implementation(start: float = 0.0, step: float = 1.0) -> Generator[int, None, None]:
    # count(10, 2) --> (12, 14, 16, 18, 20, ... infinite)
    # count(1, 0.5) --> (1, 1.5, 2.0, 2.5, ... infinite)
    n = start
    while True:
        yield n
        n += step


if __name__ == '__main__':
    zero_to_100k = range(100_001)
    count_gen = count_implementation(step=0.5)
    print(getsizeof(count_gen))  # 112 bytes.
    print(getsizeof([x for x in zero_to_100k]))  # ~0.824456 megabytes (depending on many factors).

    for _ in zero_to_100k:
        print(next(count_gen))
