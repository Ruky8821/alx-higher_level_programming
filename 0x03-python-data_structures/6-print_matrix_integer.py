#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    mtx = []
    for i in matrix:
        for j in i:
            print(" ".join("{:d}".format(col) for col in x))
