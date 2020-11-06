#!/usr/bin/python

import sys
import re

def print_usage():
    print("Usage: python filterwords.py <string> <int>")

def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))

if (len(sys.argv) != 3):
    print_usage()
    sys.exit("ERROR")

if hasNumbers(sys.argv[1]) == True:
    print_usage()
    sys.exit("ERROR")  
try:
    n2 = int(sys.argv[2])
    str1 = sys.argv[1]
    str1 = re.findall(r"[\w']+", str1)
    str1 = [x for x in str1 if len(x) > n2]
    print(str1)
except ValueError:
    print_usage()
    sys.exit("ERROR")