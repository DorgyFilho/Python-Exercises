#069 - Write a Python program to create and display all combinations of letters, selecting each letter from a 
# different key in a dictionary.

import itertools
a = 'a'
b = 'b'
c = 'c'
d = 'd'
dic = {1: [a,b], 2:[c,d]}
for union in itertools.product(*[dic[k] for k in sorted(dic.keys())]):
    print(''.join(union))