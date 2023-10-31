#!/usr/bin/python3
def print_last_digit(number):
    numstr = str(abs(number))
    numarr = []

    for items in numstr:
        numarr.append(int(items))

    for x in range(0, len(numarr)):
        y = numarr[x]
        if x == (len(numarr)-1):
            print("{}".format(y), end='')
