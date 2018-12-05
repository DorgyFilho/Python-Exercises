#059 - Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
 
#1 - Digite um número qualquer e inverta-o
num = str(input('Digite um número: ')) #Como vamos inverter o número, temos que digitar como string.
 
#2 - Crie um looping e imprima o resultado..
for i in num[::-1]: #Percorrer com o for com a variável num já acrescida do código de inversão([::-1]).
    #Isso permite que, ao imprimir o número, o resultado seja o número invertido.
    print(i, end='\t')