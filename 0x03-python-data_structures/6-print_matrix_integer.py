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
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == len(matrix[i]) - 1:
                print("{:d}".format(matrix[i][j]))
            else:
                print("{:d}".format(matrix[i][j]), end=' ')
