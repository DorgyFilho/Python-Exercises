#051 - Faça um programa que permita ao usuário digitar o
#seu nome e em seguida mostre o nome do usuário
#de trás para frente utilizando somente letras
#maiúsculas. Dica: lembre−se que ao informar o nome
#o usuário pode digitar letras maiúsculas ou
#minúsculas.
 
#1 - Digite o nome.
nome = input('Digite o seu nome em letras maiúsculas ou minúsculas, pois o resultado será em maiúsculas: ').upper()
#Função upper() para garantir que o resultado seja em letra maiúscula.
 
#2 - Utilize o recurso [::-1] para inverter o nome.
nomeInv = nome[::-1]
 
#3 - Imprima o resultado.
print(nomeInv)