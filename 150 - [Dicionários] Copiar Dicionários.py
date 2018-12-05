#150 - Write a Python script to merge two Python dictionaries.

d1 = {'1':'Games', '2':'Music'}
d2 = {'3':'Books', '4':'Racing'}
d = d1.copy()
d.update(d2)
print(d)