#183 - Sequential Search

box = [1,2,3,4,5]
num = int(input('Search: '))
x = 0
found = False
while x < len(box):
    if box[x] == num:
        found = True
        break
    x += 1

if found:
    print('Number {} found in box {}'.format(num, box[x]))
else:
    print('Not Found.')