#!/usr/bin/python

import sys


def print_usage():
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("     python operations.py 10 3")


if len(sys.argv) < 3:
    print_usage()

elif len(sys.argv) > 3:
    print("InputError: too many arguments\n")
    print_usage()

else:
    try:
        n1 = int(sys.argv[1])
        n2 = int(sys.argv[2])
        print("Sum:".ljust(11), n1 + n2)
        print("Difference:".ljust(11), n1 - n2)
        print("Product:".ljust(11), n1 * n2)
        if n2 == 0:
            print("Quotient:".ljust(11), "ERROR (div by zero)")
            print("Remainder:".ljust(11), "ERROR (modulo by zero)")
        else:
            print("Quotient:".ljust(11), n1 / n2)
            print("Remainder".ljust(11), n1 % n2)
    except ValueError:
        print("InputError: only numbers\n")
        print_usage()
