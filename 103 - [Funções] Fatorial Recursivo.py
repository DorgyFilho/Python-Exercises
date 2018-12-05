#103 - Faça um programa em python que calcule o fatorial por meio de função recursiva.

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fat = n*fatorial(n-1)
        print('{}! = {}'.format(n, fat))
    return fat

n = int(input('Número: '))
ret = fatorial(n)
print(ret)