#231 - Search Keys.

def searchName(arch):
    dic = {}
    Items = arch.readlines()
    Words = []
    arch.close()

    for i in Items:
        Words.append(i.strip())

    i = 0
    for key in Words:
        i += 1
        dic[i] = key

    name = input('Search the key: ')
    for k, v in dic.items():
        if v == name:
            return '{}'.format(dic[k])
        else:
            return False

arch = open(input('File: '), 'r')
Play = searchName(arch)
print(Play)
