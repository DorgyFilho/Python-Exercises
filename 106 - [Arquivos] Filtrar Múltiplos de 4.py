#106 - Crie um programa que filtre números múltiplos de 4 e armazene-os em um arquivo.

multi4 = open('/home/dorginho/multi4.txt','w')
pares = open('/home/dorginho/pares.txt', 'r')
leitura = pares.readlines()
pares.close()

for i in leitura:
    if int(i)%4 == 0:
        multi4.writelines(i)

multi4.close()
print('Programa Encerrado.')