def maxNum(message, *num):
    maximum = None
    for k in num:
        if maximum == None or maximum < k:
            maximum = k
    return message, maximum

num = list(range(1,101))
print(maxNum('Max: ', *num))