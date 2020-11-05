#!/usr/bin/python

t = (19, 42, 21)

str1 = ""
count = 0

for i in t:
    if i == t[-1]:
        str1 += str(i)
    else:
        str1 += str(i) + ", "
    count += 1

print("The", count, "numbers are:", str1)
