#108 - Escreva um programa que receba o nome de um arquivo pela linha
# de comando e que imprima todas as linhas desse arquivo.

arq = open('/home/dorginho/impares.txt', 'r')
for i in arq:
    print(i)

arq.close()
