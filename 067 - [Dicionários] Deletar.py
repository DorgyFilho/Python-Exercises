#067 - Write a Python program to remove a key from a dictionary.

dic = {1: 'Dorgival', 2: 'Python', 3: 'Play'}
chave = int(input('Digite uma chave: '))
if chave in dic:
    del (dic[chave])
    print(dic)
else:
    print('Chave indisponível.')