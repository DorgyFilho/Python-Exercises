#028 - Faça um programa que escreve uma
#frase digitada pelo usuário em um
#arquivo. Em seguida o programa deve ler
#e imprimir o conteúdo desse arquivo

arq = open('/home/dorginho/teste.txt', 'w')
palavra = arq.write(input('Escreva aqui: '))
arq.close()