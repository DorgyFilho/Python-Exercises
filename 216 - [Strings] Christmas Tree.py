#1 - Height

Hei = eval(input('Height: '))

line = 0

while line < Hei: #Creating the christmas tree's format.
    count = 0
    while count < Hei - line:
        print(end=' ')
        count += 1

#2 - Create a Christmas Tree.    
    count = 0
    while count < 2*line + 1:
        print(end='*')
        count += 1
    
    print()
    line += 1
