#!/usr/bin/python3
""" find peak mod """


def find_peak(list_of_integers):
    """ find peak impl """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # Move towards the direction of a higher neighbor on the left
            high = mid
        else:
            # Move towards the direction of a higher neighbor on the right
            low = mid + 1

    return list_of_integers[low]
