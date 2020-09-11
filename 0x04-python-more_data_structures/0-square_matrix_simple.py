#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrixx = matrix.copy()
    for i in range(len(matrixx)):
        matrixx[i] = list(map(lambda pow: pow ** 2, matrixx[i]))
    return matrixx
