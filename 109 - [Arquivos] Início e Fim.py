#109 - Modifique o programa do exercício 9.1 para que receba mais dois
# parâmetros: a linha de início e a de fim para impressão. O programa deve impri-
# mir apenas as linhas entre esses dois valores (incluindo as linhas de início e fim).

arq = open('/home/dorginho/pares.txt', 'r')
lista = arq.readlines()
l1 = lista[0]
l2 = lista[-1]
print(l1)
print(l2)
arq.close()