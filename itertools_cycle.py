import random
import typing
import collections.abc

"""
Arguments:
    iterable

Yield elements from the iterable until it is exhausted, then repeat the sequence indefinitely.

"""


def cycle_implementation(iterable: collections.abc.Iterable) -> [typing.Any, None, None]:
    # cycle(['A', 'B', 'C'] --> 'ABCABCABCABCABC'
    cached = []
    for element in iterable:
        yield element
        cached.append(element)
    while cached:
        for element in cached:
            yield element


if __name__ == '__main__':
    items = [random.choice(['A', 'Z', 'C', 'D', 'E']) for x in range(10)]
    gen = cycle_implementation(items)
    print(f"Item selection was: {items}")
    yielded = []
    for _ in range(1000):
        yielded.append(next(gen))

    print(yielded)

