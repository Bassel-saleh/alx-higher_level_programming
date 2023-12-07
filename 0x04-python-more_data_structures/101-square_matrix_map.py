#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda sub_mat: list(map(lambda x: x ** 2, sub_mat)), matrix))
