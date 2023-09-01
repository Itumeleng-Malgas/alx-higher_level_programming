#!/usr/bin/python3
"""

Defines a function that divides all elements of a matrix.

"""


def matrix_divided(matrix, div):
    """
        Returns a new matrix: All elements of the matrix should be divided
        by div, rounded to 2 decimal places.

    """
    if not isinstance(matrix, list) or \
        not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)            

    return new_matrix
