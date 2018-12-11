#232 - Triangle Area

def Area(b, h):
    A = (b*h)/2
    return 'Result: ' f'{A}'

b = int(input('Base: '))
h = int(input('Height: '))
Result = Area(b,h)
print(Result)