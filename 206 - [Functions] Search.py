def search(box, num):
    for x,y in enumerate(box):
        if y == num:
            return f'{y}' " found in a box " f'{x}'
    
    return False

box = list(range(1,101))
num = int(input('Number: '))
print(search(box, num))