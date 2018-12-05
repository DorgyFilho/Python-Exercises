import random
import time

num1 = list(range(0,10))
num2 = list(range(0,10))

random.shuffle(num1)
random.shuffle(num2)

chance = 5
while chance > 0:
    d = random.choice(num1)
    u = random.choice(num2)
    num = d,u
    chance -= 1
    time.sleep(1)
    if not (d == 0 and u == 0 and len(num) == 2):
        print(f'{d}',f'{u}')
        continue
    else:
        chance -= 1
        time.sleep(1)
        if chance == 0:
            print(f'{d}',f'{u}')
            break