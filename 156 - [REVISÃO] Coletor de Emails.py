#156 - REVISÃO Coletor de E-mails.

demo = ''

def verifica(email):
    validos = []
    texto = demo
    for i in range(len(email)):
        email[i] = email[i].replace('(at)', '@')
        email[i] = email[i].replace('[at]', '@')

        temp = email[i]
        var = ''

        for char in temp:
            if char.isalpha():
                var = var + char
            elif char.isnumeric():
                var = var + char
            elif char == '@':
                var = var + char
            elif char == '-':
                var = var + char
            elif char == '_':
                var = var + char
            elif char == '.':
                var = var + char
            
        var = var[:-2]

        if len(var) >= 5:
            ar = var.find('@')
            p = var[ar::].find('.')
            p = p + ar
            if ar < p:
                validos.append(var)
    
    return validos

def filtraEmails(texto):
    texto = texto.split('\n')
    demo = texto
    email = []

    for elem in texto:
        if '@' in elem:
            email.extend(elem.split(' '))
        elif '(at)' in elem:
            email.extend(elem.split(' '))
        elif '[at]' in elem:
            email.extend(elem.split(' '))
    
    Email = []

    for line in email:
        if '@' in line:
            Email.append(line)
        elif '(at)' in line:
            Email.append(line)
        elif '[at]' in line:
            Email.append(line)
    
    Email = verifica(Email)

    return Email

arq = open('/home/dorginho/teste.txt', 'r', encoding = 'ISO-8859-1')
mail = arq.read()
arq.close()
Res = filtraEmails(mail)
tam = len(Res)
print('E-mails detectados: {}'.format(tam))
if tam > 0:
    print('{:50}'.format('E-Mails Válidos'))
    print('#'*50)
    for mails in Res:
        print(mails)

print('#'*50)


