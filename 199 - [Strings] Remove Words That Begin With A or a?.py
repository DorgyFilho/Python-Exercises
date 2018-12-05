def f(elem):
    if elem[0] == 'A' or elem[0] == 'a':
        return False
    else:
        return True

words = ['Alucard', 'Soma', 'Cruz', 'adhoc']
l = filter(f, words)
f = lambda elem: elem[0] != 'a' and elem[0] != 'A'

elem = input('Element: ')
print(f(elem))