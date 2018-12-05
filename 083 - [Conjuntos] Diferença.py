#083 - Write a Python program to create set difference.

con1 = [1,2,3,4]
con2 = [5,1,2,7]
dif = set(con1).difference(con2)
dif2 = set(con2).difference(con1)
print(dif)
print(dif2)