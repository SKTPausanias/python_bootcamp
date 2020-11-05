#!/usr/bin/python

import sys

string = ' '.join(sys.argv[1:])
string = string[::-1]

print(string.swapcase())
