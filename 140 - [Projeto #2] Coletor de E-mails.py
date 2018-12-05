#140 - Parser de E-mails.

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

    for line in texto:
        if '@' in line:
            email.extend(line.split(' '))
        elif '[at]' in line:
            email.extend(line.split(' '))
        elif '(at)' in line:
            email.extend(line.split(' '))
    
    Email = []

    for linha in email:
        if '@' in linha:
            Email.append(linha)
        elif '[at]' in linha:
            Email.append(linha)
        elif '(at)' in linha:
            Email.append(linha)

    Email = verifica(Email)

    return Email

arq = open("/home/dorginho/teste.txt", "r", encoding = "ISO-8859-1")
s = arq.read()
arq.close()

listaResultados = filtraEmails(s)
tam = len(listaResultados)
print("Quantidade de emails detectados: ", tam)
if tam > 0:
	print("Emails detectados: ")
	print("#####################################")
	for elem in listaResultados:
		print(elem)
print("#####################################")