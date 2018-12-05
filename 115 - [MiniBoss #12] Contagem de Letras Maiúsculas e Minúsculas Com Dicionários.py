#115 - Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. 
#Suppose the following input is supplied to the program:
#Hello world!
#Then, the output should be:
#UPPER CASE 1
#LOWER CASE 9 

dic = dict()
big = 0
small = 0
num = 0
frase = input('Digite uma frase: ').replace(' ','')
for i in frase:
    if i.isupper():
        big += 1
    elif i.islower():
        small += 1
    elif i.isdigit():
        num += 1

dic['MAIÚSCULAS'] = big
dic['MINÚSCULAS'] = small
dic['NÚMEROS'] = num

print(dic)