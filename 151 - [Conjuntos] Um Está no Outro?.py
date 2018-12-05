#151 - Write a Python program to test whether every element in s is in t and every element in t is in s.

#Dicas: subcon representa <= e supercon representa >=.

A = set(['Dorgival', 'Cecilia'])
B = set(['Shiro', 'Dorgival'])
C = set(['Shiro'])
isSub = A <= B
print(isSub)
isSuper = B >= A
print(isSuper)
isSub2 = C <= B
print(isSub2)
isSuper2 = B >= C
print(isSuper2)