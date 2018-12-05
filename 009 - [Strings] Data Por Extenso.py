#009 - Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e 
#imprima a data com o nome do mês por extenso.
#Data de Nascimento: 29/10/1973
#Você nasceu em  29 de Outubro de 1973.

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 
'Outubro', 'Novembro', 'Dezembro']

dia, mes, ano = input('Escreva a data de nascimento no formato DD/MM/AAAA: ').split('/')

print('Você nasceu no dia {} de {} de {}'.format(dia, meses[int(mes)-1], ano))