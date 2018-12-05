#134 - Dado duas string `a` e `b`,  trocar os 2 primeiros caracteres entre as variáveis
# e retornar uma única string separada por espaço como no exemplo:
#
# "pezzy", "firm" ----> "fizzy perm"

def troca(a, b):
    a1 = b[:2] + a[2:]
    b1 = a[:2] + b[2:]
    return a1 + ' ' + b1

a = input('Palavra 1: ')
b = input('Palavra 2: ')
print(troca(a,b))
