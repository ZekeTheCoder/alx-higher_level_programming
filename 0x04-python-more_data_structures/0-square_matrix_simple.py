#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = []
    for x in matrix:
        squared.append(list(map(lambda x: x**2, x)))
    return (squared)
