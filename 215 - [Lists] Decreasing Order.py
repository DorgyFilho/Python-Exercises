def decOrder():
    List = [1,2,3,4,5]
    End = 5
    while End > 1:
        change = False
        x = 0
        while x < (End - 1):
            if List[x] < List[x+1]:
                change = True
                Temp = List[x]
                List[x] = List[x+1]
                List[x+1] = Temp
            x += 1
        if not change:
            print("Didn't Change.")
            break
        End -= 1
    
    revList = []
    for p in List:
        revList.append(p)
    print(revList)

decOrder()