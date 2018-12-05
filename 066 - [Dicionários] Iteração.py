#066 - Write a Python program to iterate over dictionaries using for loops.

dic = {1: 'Dorgival', 2: 'Python', 3: 'Play'}
for chave, valor in dic.items():
    print('{} - {}'.format(chave, dic[chave]))