#006 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
#Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
#Fatorial de: 5
#5! =  5 . 4 . 3 . 2 . 1 = 120

fat = 1
num = int(input('Digite um número: '))
valor = num

print('{}! = '.format(valor), end=' ')
while valor > 0:
    print('{}'.format(valor), end=' ')
    print('.' if valor > 1 else '=', end=' ')
    fat *= valor
    valor -= 1
print('{}'.format(fat))