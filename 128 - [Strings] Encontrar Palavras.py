#128 - Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, 
# if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. 
# Go to the editor 
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

def aparece(frase):
    Snot = frase.find('not')
    Spoor = frase.find('poor')

    if Spoor > Snot and Spoor > 0 and Snot > 0:
        frase = frase.replace(frase[Snot:Spoor+4], 'good')
        return frase
    else:
        return frase

frase = input('Digite uma frase: ')
print(aparece(frase))