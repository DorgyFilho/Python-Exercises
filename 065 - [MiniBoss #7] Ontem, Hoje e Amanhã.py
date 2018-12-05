#065 - Write a Python program to print yesterday, today, tomorrow.

import datetime
hoje = datetime.datetime.now()
ontem = hoje - datetime.timedelta(days = 1)
amanha = hoje + datetime.timedelta(days = 1)
print('Ontem foi {}'.format(ontem))
print('Hoje é {}'.format(hoje))
print('Amanhã será {}'.format(amanha))