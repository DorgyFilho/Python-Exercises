Hei = int(input('Height: '))

for let in range(Hei):
    for ad in range(Hei-let):
        print(end=' ')
    
    for tree in range(2*let+1):
        print(end='*')
    
    print()