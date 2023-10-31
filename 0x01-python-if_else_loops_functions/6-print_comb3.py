#!/usr/bin/python3
for n in range(0, 10):
    for m in range(n + 1, 10):
        print("{}{}".format(n, m), end=', '
              if not(n == 8 and m == 9) else '')
