#!/usr/bin/python3
"""This function finds a peak in list of unsorted integers"""


def find_peak(list_of_integers):
    """Returns a peak in a list of unsorted integers."""
    list_size = len(list_of_integers)

    if list_size == 0:
        return None

    low = 0
    high = list_size - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]
