#027 - Crie um algoritmo que lê um conjunto de nomes de um arquivo ‘nomes.txt’. Esse
# algoritmo deverá separar os nomes que iniciam com vogal e escrever em um novo
# arquivo ‘vogal.txt’, enquanto que os nomes que iniciam com consoante devem ser
# escritos no arquivo ‘consoante.txt’.

arq = open('/home/dorginho/nomes.txt', 'r')
lNome = arq.readlines()
arq.close()

vog = []
con = []

for start in lNome:
    if 'A' in start or 'E' in start or 'I' in start or 'O' in start or 'U' in start:
        vog.append(start)
    else:
        con.append(start)

vogal = open('/home/dorginho/vogal.txt', 'w')
conso = open('/home/dorginho/conso.txt', 'w')
vogal.writelines(vog)
conso.writelines(con)
vogal.close()
conso.close()
     