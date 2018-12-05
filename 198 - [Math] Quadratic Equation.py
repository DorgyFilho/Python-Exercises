while True:
    ax = int(input('ax²: '))
    if ax == 0:
        print('Invalid Equation')
        break
    else:
        bx = int(input('bx: '))
        c = int(input('c: '))

    delta = (bx**2) - (4*ax*c)
    if delta < 0:
        print('The equation has no result.')
        break
    elif delta == 0:
        r = (-bx + (delta**0.5)/(2*ax))
        print('Result: 'f'{r}')
        break
    else:
        r1 = (-bx + (delta**0.5)/(2*ax))
        r2 = (-bx - (delta**0.5)/(2*ax))
        print('Result 1: 'f'{r1}')
        print('Result 2: 'f'{r2}')
        break
