#148 - Write a Python program to remove duplicates from Dictionary.

meudic = {'1':'Dorginho', '2':'Shiro', '3':'Cecilia', '4': 'Saulo', '5':'Dorginho'}
novoDic = {}
for c, v in meudic.items():
    if v not in novoDic.values():
        novoDic[c] = v

print(novoDic)
