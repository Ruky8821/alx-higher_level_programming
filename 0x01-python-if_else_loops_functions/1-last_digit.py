#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numstr = str(abs(number))
numarr = []
str = "Last digit of "
for items in numstr:
    numarr.append(int(items))

for x in range(0, len(numarr)):
    y = numarr[x]
    if x == (len(numarr)-1):
        if number > 0:
            if y > 5:
                print(f"Last digit of {number} is {y} and is greater than 5")
            elif y == 0:
                print(f"Last digit of {number} is {y} and is 0")
            else:
                print(f"{Last digit of {number} is {y} and is less than 6 and not 0")
        elif number < 0:
            if y == 0:
                print(f"Last digit of {number} is {y} and is 0")
            else:
                print(f"Last digit of {number} is -{y} and is less than 6 and not 0")
        else:
            print(f"Last digit of {number} is {y} and is 0")


