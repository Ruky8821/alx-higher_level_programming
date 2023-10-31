#!/usr/bin/python3
def uppercase(str):
    upp = ""
    for lett in str:
        if 97 <= ord(lett)  <= 122:
            upp = upp + chr(ord(lett) - 32)
        else:
            upp = upp + lett
    print("{}".format(upp))

