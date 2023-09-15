#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix

    Args:
        matrix: matrix to be squared

    Returns:
        new matrix with elements squared
    """
    if matrix is None or len(matrix) == 0:
        return
    new_matrix = []
    for element in matrix:
        new_matrix.append([x**2 for x in element])
    return(new_matrix)
