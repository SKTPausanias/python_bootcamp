#!/usr/bin/python

import sys


def is_intstring(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


if (len(sys.argv) == 1):
    sys.exit()

if (len(sys.argv) > 2):
    sys.exit("ERROR")

if (is_intstring(sys.argv[1]) is False):
    sys.exit("ERROR")

else:
    n = int(sys.argv[1])
    if (n == 0):
        print("I'm Zero.")
    elif (n % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")
