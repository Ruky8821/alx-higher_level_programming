#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for y in my_string:
        if y not in ('c', 'C'):
            new += y
    return new


