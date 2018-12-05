#003 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, 
# dezenas e unidades do mesmo. Observando os termos no plural a colocação do "e", da vírgula entre outros.
# Exemplo: 326 = 3 centenas, 2 dezenas e 6 unidades 12 = 1 dezena e 2 unidades 
# Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16


numero = int(input('Digite um número menor que 1000: '))
if numero >= 1000 or numero < 0:
    print('Erro! Só é aceito um número menor que esteja entre 1 e 999.')
else:
    numStr = str(numero)
    tamNum = len(numStr)

    if tamNum == 3:
        c = numStr[0]
        d = numStr[1]
        u = numStr[2]
        print('O número possui {} centena(s), {} dezena(s) e {} unidade(s)'.format(c,d,u))

    elif tamNum == 2:
        d = numStr[0]
        u = numStr[1]
        print('O número possui {} dezena(s) e {} unidade(s).'.format(d,u))

    elif tamNum == 1:
        u = numStr[0]
        print('O número possui {} unidade(s).'.format(u))

