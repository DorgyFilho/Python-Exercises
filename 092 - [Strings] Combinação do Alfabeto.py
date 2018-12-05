#092 - Write a Python program to get all possible two digit letter combinations from a digit (1 to 9) string.

# string_maps = {
# "1": "abc",
# "2": "def",
# "3": "ghi",
# "4": "jkl",
# "5": "mno",
# "6": "pqrs",
# "7": "tuv",
# "8": "wxy",
# "9": "z"
# }

def combo(dig):
    if dig == '':
        return []
    
    dicLet = {
    "1": "abc",
    "2": "def",
    "3": "ghi",
    "4": "jkl",
    "5": "mno",
    "6": "pqrs",
    "7": "tuv",
    "8": "wxy",
    "9": "z"
    }

    resultado = ['']
    for i in dig:
        lista = []
        for j in resultado:
            for k in dicLet[i]:
                lista.append(j+k)
            resultado = lista
    return resultado

digito = input('Digite um número: ')
Resultado = combo(digito)
print('O resultado é {}'.format(Resultado))