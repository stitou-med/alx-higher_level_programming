#!/usr/bin/python3
"""A module that divides a matrix by a given number"""


def matrix_divided(matrix, div):
    new_matrix = []
    """A function that divides a matrix

    Args:
        matrix(list of list): matrix to be divided
        div(int or float): number to divide the matrix with
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div is 0:
        raise ZeroDivisionError("division by zero")

    wrong_type = 'matrix must be a matrix (list of lists) of integers/floats'
    wrong_size = 'Each row of the matrix must have the same size'
    if matrix is None or len(matrix) is 0 or len(matrix[0]) is 0:
        raise TypeError(wrong_type)
    then = len(matrix[0])

    try:
        for count, row in enumerate(matrix):
            if not isinstance(row, list):
                raise TypeError(wrong_type)
            if len(row) != then:
                raise TypeError(wrong_size)
            then = len(row)
            new_matrix.append(row[:])
            for ind, item in enumerate(row):
                if not isinstance(item, (int, float)):
                    raise TypeError(wrong_type)
                new_matrix[count][ind] = round(item / div, 2)
    except ValueError:
        pass
    else:
        return (new_matrix)
