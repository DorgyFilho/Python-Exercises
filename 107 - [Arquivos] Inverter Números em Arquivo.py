#107 - Crie um programa que inverta a ordem das linhas do arquivo pares.
# txt. A primeira linha deve conter o maior número; e a última, o menor.

arq = open('/home/dorginho/pares.txt', 'r')
saida = open('/home/dorginho/saida.txt', 'w')
pares = arq.readlines()
pares.reverse()
arq.close()

for i in pares:
    saida.writelines(i)

saida.close()


