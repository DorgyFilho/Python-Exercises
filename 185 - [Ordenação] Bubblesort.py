#185 - Bubblesort

def bubble(box):
    for p in range(len(box)-1,0,-1):
        for x in range(p):
            if box[x] > box[x+1]:
                temp = box[x]
                box[x] = box[x+1]
                box[x+1] = temp

box = [4,7,1,3,2]
bubble(box)
print(box)

