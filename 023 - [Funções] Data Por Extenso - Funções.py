#023 - Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e 
#devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e 
#retorne NULL caso a data seja inválida.

def mesExt(mes):
    mes = int(mes)
    meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
    'Outubro', 'Novembro', 'Dezembro')
    if 0 < mes <= 12:
        return meses[int(mes)-1]
    else:
        return 'NULL'

dia, mes, ano = input('Data no formato DD/MM/AAAA: ').split('/')
print('Você nasceu no dia {} de {} de {}'.format(dia, mesExt(mes), ano))