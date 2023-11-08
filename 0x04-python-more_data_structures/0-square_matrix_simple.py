#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda new: list(map(lambda x: x*x, new)), matrix))
    '''
    new = matrix

    for x in new:
        print("[", end='')
        for y, z in enumerate(x):
            print("{:d}".format(z*z), end='')
            if y < len(x) - 1:
                print(", ", end='')
        print("]", end='')
    return new
    '''
