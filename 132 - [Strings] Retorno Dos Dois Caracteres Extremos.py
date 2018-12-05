#132 - Dado uma string qualquer `s`, retonar uma string
# composta dos 2 primeiros e os 2 últimos caracteres, exemplo:
#
# panela ----> pala
# bala   ----> bala
# mao    ----> maao
# ja     ----> jaja
#
# Caso a string `s` contenha menos que 2 caracteres,
# retornar "" (string de cumprimento zero). 

def palavra(str1):
    if len(str1) < 2:
        return ''
    else:
        return str1[:2] + str1[-2:]

str1 = input('Palavra: ')
print(palavra(str1))
