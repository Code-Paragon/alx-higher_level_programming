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
    # Convert integers to strings and join with spaces
        row_str = ' '.join(map(str, row))
        print("{}".format(row_str))
