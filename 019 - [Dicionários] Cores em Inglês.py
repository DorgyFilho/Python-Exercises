#019 - Faça um programa que traduza uma cor para o inglês e que mostre uma mensagem caso a cor digitada
#não esteja no dicionário.

cores = {'AMARELO':'YELLOW', 'PRETO': 'BLACK', 'BRANCO': 'WHITE'}

cor = input('Digite a cor: ').upper()

busca = cores.get(cor, 'Cor inexistente no dicionário')

print('Resultado da busca: {}'.format(busca))