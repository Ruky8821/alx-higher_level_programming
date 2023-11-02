#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":

    hidden_name = dir(hidden_4)
    for i in hidden_name:
        if i[0] != "__":
            print(i)
