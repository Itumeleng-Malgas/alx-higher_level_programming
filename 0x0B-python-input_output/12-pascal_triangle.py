#!/usr/bin/python3
"""define pascal's triangle"""


def pascal_triangle(n):
    """ returns a list of list representing the Pascal’s triangle of n"""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # The first element is always 1

        for j in range(1, i):
            new_element = prev_row[j - 1] + prev_row[j]
            new_row.append(new_element)

        new_row.append(1)  # The last element is always 1
        triangle.append(new_row)

    return triangle
