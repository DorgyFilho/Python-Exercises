#184 - Sequential Search 2

def search(num):
    box = list(range(1,101))
    x = 0
    found = False
    while x < len(box):
        if box[x] == num:
            found = True
            break
        x += 1
    if found:
        return 'Number {} found in box {}'.format(num, box[x])
    else:
        return 'Not Found'

num = int(input('Search: '))
print(search(num))
