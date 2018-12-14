# 250 - Binary Search
 
# 1 - Crie uma lista com o método list()
numeros = list(range(1000))
 
# 2 - Crie uma variável booleana denominada 'achou', cujo valor seja False.
achou = False
 
# 3 - Crie duas variáveis denominadas 'inicio' e 'fim', cujos valores sejam,
# respectivamente, 0 e comprimento da lista.
inicio = 0
fim = len(numeros)
 
num = int(input('Digite um número: '))
if num == -999:
    print('Busca Encerrada.')
 
# 5 - Crie um while que funcione até que o número seja encontrado ou não.
while True:
    meio = (inicio + fim) // 2
    if num == meio:
        print('Número encontrado na {}° posição.'.format(meio))
        achou = True
        break
    elif num < meio:
        fim = meio - 1
    elif num > meio:
        inicio = meio + 1
 
    # 5 - Veja a posição do número buscado.
    if inicio > fim:
        print('Programa encerrado. Número não encontrado.')
        break