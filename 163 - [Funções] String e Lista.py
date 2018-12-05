#163 - Exercício 8.12 - Nilo Menezes: Página 174

def strLista(lista, s):
    if s in lista:
        return True
    else:
        return False

lista = ['AB', 'CD', 'EF', 'GHI', 'JKL', 'LMN', 'OPQ', 'RST', 'UVW', 'XYZ']
s = input('Digite uma sequência de letras. Ex: AB, AC etc: ').upper()
print(strLista(lista, s))