import types

def Type(List):
    for i in List:
        if type(i) == str:
            print(i)
        else:
            print('List: 'f'{List}')
            for j in i:
                print(j)
            return 'Turn Off'


List = ['a', ['a','b','c'], 'b']
print(Type(List))
