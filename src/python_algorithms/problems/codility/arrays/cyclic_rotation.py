"""
URL: https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
"""


def cyclic_rotation(a, k):
    """
    Rotate the array A by k steps
    :param a: an array of integers
    :param k: number of times to shift right
    :return: the rotated array
    """
    # A is empty
    if not len(a):
        return a

    # netK is the net number of shifts to apply (omits spinning round and round)
    net_k = (len(a) + k) % len(a)
    if net_k > 0:
        head = a[len(a) - net_k:]
        tail = a[:-net_k]
        return head + tail
    else:
        return a
