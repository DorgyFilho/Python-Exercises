import types

def funcMethod(name):
    Type = type(name)
    if Type == str:
        return 'String'
    elif Type == float:
        return 'Floating Number'
    elif Type == dict:
        return 'Dictionary'
    elif Type == list:
        return 'List'
    elif Type == int:
        return 'Int'
    elif Type == types.BuiltinFunctionType:
        return 'Built in Function'
    elif Type == types.FunctionType:
        return 'Function'
    else:
        return str(Type)

print(funcMethod('a'))
print(funcMethod(23))
print(funcMethod(10.23))
print(funcMethod([1,2,3]))
print(funcMethod({'key':1}))
print(funcMethod(print))
print(funcMethod(True))