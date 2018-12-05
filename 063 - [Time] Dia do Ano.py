# 063 - Write a Python program to convert Year/Month/Day to Day of Year in Python.

import datetime
hoje = datetime.datetime.now()
diaDoAno = (hoje - datetime.datetime(hoje.year,1,1)).days + 1
print('O dia do ano é: {}'.format(diaDoAno))
