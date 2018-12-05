#180 - Exercício 5.26: Nilo Menezes

def resto(num, den):
    x = num
    quo = 0
    while x >= den:
        x -= den
        quo += 1
    resto = x
    return 'Num: {} / Den: {} / Rest: {}'.format(num, den, resto)

num = int(input('Num: '))
den = int(input('Den: '))
print(resto(num, den))