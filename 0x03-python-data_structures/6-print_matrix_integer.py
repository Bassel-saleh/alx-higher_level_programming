#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for rix in matrix:
        if len(rix) == 0:
            print()
        x = len(rix)
        for i in range(x):
            print("{:d}".format(rix[i]), end="\n" if i is x - 1 else " ")
