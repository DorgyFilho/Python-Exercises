# 002- Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa 
# deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer 
# pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário

a = int(input('ax²: '))
if a == 0:
    print('Erro! A variável a não pode ser igual a zero.')
else:
    b = int(input('bx: '))
    c = int(input('c: '))

numA = a
numB = b
numC = c

delta = (numB**2) - (4*numA*numC)

if delta < 0:
    print('A equação não possui raizes reais. Programa encerrado.')
elif delta == 0:
    raiz = (-numB + (delta**0.5))/2*numA
    print('A equação possui apenas uma raiz real. A raiz é {}'.format(raiz))
else:
    raiz1 = (-numB + (delta**0.5))/2*numA
    raiz2 = (-numB - (delta**0.5))/2*numA
    print('A equação possui duas raizes reais. As raizes são {:.0f} e {:.0f}'.format(raiz1, raiz2))

