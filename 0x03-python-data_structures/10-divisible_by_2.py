#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mul = []
    for i in my_list:
        if i % 2 == 0:
            mul.append(True)
        else:
            mul.append(False)
