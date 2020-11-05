#!/usr/bin/python

tupl = (0, 4, 132.42222, 10000, 12345.67)

str1 = "day_0" + str(tupl[0]) + ","
str2 = "ex_0" + str(tupl[1])
str3 = str(f'{tupl[2]:.2f}') + ","
str4 = str("{:.2e}".format(tupl[3])) + ","
str5 = str("{:.2e}".format(tupl[4]))

print(str1, str2, ":", str3, str4, str5)
