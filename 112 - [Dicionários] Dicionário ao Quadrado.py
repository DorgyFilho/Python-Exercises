#112 - Define a function which can print a dictionary where the keys are numbers between 1 and 3 
# (both included) and the values are square of keys.

#Hints:

#Use dict[key]=value pattern to put entry into a dictionary.
#Use ** operator to get power of a number.
 
dic = dict()
for i in range(1,4):
    dic[i] = i**2
print(dic)
