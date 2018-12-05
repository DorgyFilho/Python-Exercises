#114 - Write a program that accepts a sentence and calculate the number of letters and digits.
#Suppose the following input is supplied to the program:
#hello world! 123
#Then, the output should be:
#LETTERS 10
#DIGITS 3

#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input. 

dic = {}
letras = 0
numeros = 0
frase = input('Digite uma frase: ').replace(' ','')
for i in frase:
    if i.isdigit():
        numeros += 1
    else:
        letras += 1

dic['LETRAS'] = letras
dic['NUMEROS'] = numeros
print(dic)