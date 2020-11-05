#!/usr/bin/python

import datetime

time_tuple = (3, 30, 2019, 9, 25)

str1 = str(time_tuple[2]) + "-" + str(time_tuple[3])
str1 += "-" + str(time_tuple[4]) + " " + str(time_tuple[0])
str1 += ":" + str(time_tuple[1])

date_time_obj = datetime.datetime.strptime(str1, '%Y-%m-%d %H:%M')

print(f'{date_time_obj:%Y-%m-%d %H:%M}')
