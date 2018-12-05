#091 - Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.

import random
vogal = ['a','e','i','o','u']
random.shuffle(vogal)
print(''.join(vogal))