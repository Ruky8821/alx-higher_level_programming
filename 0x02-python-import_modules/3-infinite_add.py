#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    x = sys.argv[1:]
    for i in x:
        sum = sum + int(i)
    print("{}".format(sum))
