#!/usr/bin/python3
import sys

str = "and that piece of art is useful - Dora Korpar, 2015-10-19"

# print to stderr
sys.stderr.write(str + "\n")

# exit status
e_status = 1
sys.exit(e_status)
