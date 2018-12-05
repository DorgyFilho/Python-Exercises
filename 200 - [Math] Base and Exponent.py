b = int(input('Base: '))
e = int(input('Exponent: '))
res = 1 #Base
count = 0
while count < e:
    count += 1
    res *= b #Result
print('Result: 'f'{res}')