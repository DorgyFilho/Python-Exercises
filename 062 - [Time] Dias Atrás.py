#062 - Write a Python program to subtract five days from current date. Go to the editor
# Sample Date : 
# Current Date : 2015-06-22
# 5 days before Current Date : 2015-06-17

from datetime import date, timedelta
dif = int(input('Digite um número: '))
data = date.today() - timedelta(dif)
print('Data atual: {}'.format(date.today()))
print('Data de {} atrás: {}'.format(dif, data))