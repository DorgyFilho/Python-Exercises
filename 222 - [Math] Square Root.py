#226 -  Square Root Game - Only Integer

#Only Integer numbers.

def squareRoot():
    SquareList = list(range(1,101))
    a = int(input('Choose a number: '))
    b = int(input('Choose another number: '))
    exp = 1/(float(b))
    sRoot = a**exp
    if sRoot in SquareList:
        return True
    else:
        return False

print(squareRoot())

