#235 - A is Multiple of B

def isMultiple(a,b):
    if a % b == 0:
        return 'Multiple'
    else:
        return 'Not Multiple'

a = int(input('Number a: '))
b = int(input('Number b: '))
Result = isMultiple(a,b)
print(Result)