#245 - Faça um programa que mostre os n termos da Série a seguir:
#S = 1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.

n = 0
m = int(input('Number (Den): '))

total = 0

for i in range(1, m+1, 2):
    n += 1
    total += n/i
print(f'Total: {total}')