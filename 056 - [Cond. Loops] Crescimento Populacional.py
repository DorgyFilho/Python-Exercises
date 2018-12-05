#056 - . Dado um país A, com 5.000.000 de habitantes e uma taxa de natalidade de 3% ao ano, e um
#país B com 7.000.000 de habitantes e uma taxa de natalidade de 2% ao ano, calcular e imprimir
#o tempo necessário para que a população do país A ultrapasse a população do país B.
 
#1 - Crie as variáveis que receberão os respectivos dados.
a = 5000000
b = 7000000
taxaA = (3/100)
taxaB = (2/100)
 
#2 - Crie um looping para que a o país A torne-se superior em termos de quantidade populacional ao país B.
anos = 1 #Criei esta variável para que contasse a quantidade de anos necessária para que o país A
#ultrapasse o País B.
while a < b:
    a = a*(1+taxaA)
    b = b*(1+taxaB)
    anos += 1
 
#3 - Imprima o resultado.
print('C Á L C U L O  D E  C R E S C I M E N T O')
print('=========================================')
print('País A:', round(a)) #A função round é uma função de arredendamento de resultados.
print('=========================================')
print('País B:', round(b)) #Foi utilizada para que o número fosse exato.
print('=========================================')
print('Será(ão) necessário(s) {} anos para o País A ultrapassar o País B em termos populacionais.'.format(anos))