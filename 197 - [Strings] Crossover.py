import random

s1 = input('Sequence 1: ').upper()
s2 = input('Sequence 2: ').upper()

p = random.randint(0, len(s1)-1)

if len(s1) != len(s2):
    print('Errors! The strings have different len')
else:
    news1 = s1[:p] + s2[p:]
    news2 = s2[:p] + s1[p:]

print('New S1: 'f'{news1}')
print('New S2: 'f'{news2}')