#!/usr/bin/python3
def islower(c):
    while type(c) == str and len(c) == 1:
        if ord('a') <= ord(c) <= ord('z'):
            return True
        else:
            return False

