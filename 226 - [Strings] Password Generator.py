#230 - Password Generator

import string
import random

def passwordGen(size=12, char=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(char) for _ in range(size))

print(passwordGen(int(input('How much characters you want?: '))))

    
