#!/usr/bin/python3
squarematrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = squarematrix_simple(matrix)
print(new_matrix)
print(matrix)
