# 064 - Write a Python program to get days between two dates.

from datetime import date
dataA = date(2017, 11, 18)
dataB = date(2021, 11, 18)
res = dataB - dataA
print('O resultado é {}'.format(res))