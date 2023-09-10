#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers

    Args:
        matrix: integer matrix to be printed

    Returns:
        NULL
    """
    if matrix is None or len(matrix) == 0:
        return
    for row in matrix:
        for element in row:
            print("{:d}".format(element), end=' ')
        print()
