#!/usr/bin/python3
for num in range(0, 100):
    y = "{:02}".format(num)
    if num <= 98:
        print("{}".format(y), end=', ')
print("99")
