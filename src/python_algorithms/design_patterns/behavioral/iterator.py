"""
Implementation of the iterator pattern with a generator

Traverses a container and accesses the container's elements.
"""


def count_to(count):
    """
    Counts by word numbers, up to a maximum of five
    :param count: int
    :return: int
    """
    numbers = ["one", "two", "three", "four", "five"]
    for number in numbers[:count]:
        yield number
