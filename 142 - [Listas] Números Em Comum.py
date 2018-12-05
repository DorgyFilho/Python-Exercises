#142 - Write a Python function that takes two lists and returns True if they have at least one common member.

def comum(x,y):
    res = False
    for a in x:
        for b in y:
            if a == b:
                res = True
                return res

x = [1,2,3,4]
y = [3,4,5,6]
print(comum(x,y))