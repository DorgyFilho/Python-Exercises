#166 - Listagem 8.34 - Nilo Menezes: Página 181

def intervalo(maxi, mini):
    Vn = False
    while Vn == False:
        n = input('Digite um número: ')
        try:
            n = int(n)
            if mini <= n <= maxi:
                Vn = True
                return '{} é {}'.format(n, Vn)
            else:
                print('Digite um valor dentro do intervalo mencionado.')
        except:
            print('DIgite apenas números inteiros.')

mini = int(input('Digite o intervalo mínimo: '))
maxi = int(input('Digite o intervalo máximo: '))
print(intervalo(maxi, mini))