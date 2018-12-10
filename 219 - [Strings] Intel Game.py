import random
import string

def generator(tam=12, characters=string.ascii_uppercase + ' '):
    return ' '.join(random.choice(characters) for _ in range(tam))

print(generator())