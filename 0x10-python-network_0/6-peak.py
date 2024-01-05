#!/usr/bin/python3
""" find peak mod """


def find_peak(list_of_integers):
    """ find peak impl """
    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        # Move towards the direction of a higher neighbor
        high = (mid if list_of_integers[mid] > list_of_integers[mid + 1]
                else mid + 1)

    return list_of_integers[low]
