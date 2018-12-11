#236 - Triangle Type.

def triangleType(a,b,c):
    if a == b == c:
        return 'The Triangle is Equilateral.'
    elif (a == b and a != c) or (a == b and b != c) or (a != b and a == c) or (a != b and b == c):
        return 'The Triangle is Isosceles.'
    else:
        return 'The Triangle is Scalene.'

a = int(input('A-number: '))
b = int(input('B-number: '))
c = int(input('C-number: '))
Result = triangleType(a,b,c)
print(Result)