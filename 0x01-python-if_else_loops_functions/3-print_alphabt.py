#!/usr/bin/python3
n = ""
for j in range(97, 123):
    if chr(j) == 'e' or chr(j) == 'q':
        continue
    n += chr(j)
print("{}".format(n), end='')
