#061 Write a Python script to display the
# a) Current date and time
# b) Current year
# c) Month of year
# d) Week number of the year
# e) Weekday of the week
# f) Day of year
# g) Day of the month
# h) Day of week

import time
import datetime

#1 - Data e Hora
hAtual = datetime.datetime.now()
print('Hora atual: {}'.format(hAtual))

#2 - Ano Atual
ano = datetime.datetime.now().strftime('%Y')
print('O ano é {}'.format(ano))

#3 - Mês atual
mes = datetime.datetime.now().strftime('%B')
print('O mês é {}'.format(mes))

#4 - Número da semana do ano
semana = datetime.datetime.now().strftime('%U')
print('O número da semana é {}'.format(semana))

#5 - Dia da Semana - NOme
dSem = datetime.datetime.now().strftime('%A')
print('O dia da semana é {}'.format(dSem))

#6 - Dia do Ano
dAno = datetime.datetime.now().strftime('%j')
print('O dia do ano é {}'.format(dAno))

#7 - Dia do Mês
dMes = datetime.datetime.now().strftime('%d')
print('O dia do mês é {}'.format(dMes))

#8 - Dia da Semana - Número
dSema = datetime.datetime.now().strftime('%w')
print('O número do dia da semana é {}'.format(dSema))
