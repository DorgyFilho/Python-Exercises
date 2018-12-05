#049 - Uma empresa de pesquisas precisa tabular os
#resultados da seguinte enquete feita a um grande
#quantidade de organizações: "Qual o melhor Sistema
#Operacional para uso em servidores?" As possíveis
#respostas são:
#1- Windows XP 2- Unix 3- Linux 4- Netware 5- Mac OS 6- Outro
#Você deve desenvolver um programa em Python que
#leia as respostas da enquete e informe ao final o
#resultado da mesma. O programa deverá ler os valores
#até ser informado o valor 0 (zero), que encerra a
#entrada dos dados. Não deverão ser aceitos valores
#além dos válidos para o programa (0 a 6).
#Os valores referentes a cada uma das opções devem
#ser armazenados em uma lista. Após os dados terem
#sido completamente informados, o programa deverá
#calcular a percentual de cada uma das respostas e
#informar o vencedor da enquete.
 
#1 - Crie uma lista com as opções de voto.
sistema = ['Win XP', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
 
#2 - Crie um vetor denominado 'votossys' cujo valor seja '[0]*6'. Corresponde a quantidade
#de votos que cada opção terá.
votossys = [0]*6
 
#3 - Crie uma variável denominada votos, cujo valor inicial seja -1.
#O menos 1 servirá para que mais adiante, quando for usada a acumulação de votos,
#terei que subtrair 1 para que o valor seja devidamente lido e com isso, evitar
#erros na contagem de votos.
votos = -1
 
#4 - Crie a variável 'totalVotos', cujo valor inicial seja 0.
totalVotos = 0
 
#5 - Crie uma variável denominada 'i', cujo valor inicial seja 0.
print('{:100}'.format('QUAL O MELHOR SISTEMA OPERACIONAL PARA SERVIDORES?'))
print('='*100) #Separador.
i = 0
#Crie um looping for para percorrer a lista de opções.
for k in range(len(sistema)): #Gerado   r de opções.
    print(k+1, '--->', '{}'.format(sistema[k])) #Mostre-me as opções.
    i += 1 #Variável contadora.
 
#6 - Crie um while para que a votação aconteça. Se digitar 0, a votação encerra.
while votos != 0:
    votos = int(input('Digite o seu voto entre 1 e 6 ou 0 para sair: '))
    if not (0 < votos < 7): #Se não for entre 1 e 6, continue até votar.
        print('Digite apenas opções de 1 a 6 ou 0 para sair.')
        continue #O laço repetirá até que o 0 seja digitado.
    if votos == 0: #Encerre a votação.
        break #Votação encerrada.
    votossys[votos - 1] += 1 #Conte os votos.
    totalVotos += 1 #Acumular votos.
 
#7 - Crie um looping for para percorrer a lista de sistemas e detectar o sistema com
#a maior quantidade de votos.
print('{:100}'.format('RESULTADO DA ENQUETE')) #Mensagem de exibição.
print('='*100) #Separador.
maiorvoto = 0 #Obter o sistema que apresentar maior votação.
i = 0 #Contadora
for k in range(len(sistema)):
    print('{}  ---->  {}  ---->  {:.2f}%'.format(sistema[i], votossys[i], votossys[i]/float(totalVotos)*100))
    if votossys[i] > votossys[maiorvoto]:
        maiorvoto = i
    i += 1
 
#8 - Exiba o total de votos.
print("="*100) #Organizador.
print('Total de votos: {}'.format(totalVotos))
 
#9 - Exiba o vencedor da enquete.
print('='*100) #Separador
print('O vencedor da enquete foi o sistema {}, com {} votos, correspondendo ao percentual de {:.2f}% '
      'dos votos válidos.'.format(sistema[maiorvoto], votossys[maiorvoto],
                                 (votossys[maiorvoto])/float(totalVotos)*100))