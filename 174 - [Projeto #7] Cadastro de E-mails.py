emails = []
alterada = False

def pede_id(padrao=''):
    ident = input('Digite o seu identificador: ')
    if ident == '':
        ident = padrao
    return ident

def pesquisa(ident):
    pesq = ident
    for p, e in enumerate(emails):
        if e[0] == pesq:
            return p
def novo():
    global emails, alterada
    ident = pede_id()
    server = '@dorgyenterprises.com'
    email = ident+server
    senha = input('Digite a sua senha: ')
    if email not in emails:
        emails.append([email, senha])
        alterada = True
    else:
        print('E-mail já cadastrado em nosso servidor.')
        alterada = False

def mostraEmails():
    global emails
    print(emails)

def main():
    while True:
        print('''Escolha uma das opções abaixo\n1-Cadastrar\n2-Mostrar Emails\n3-Sair\nEscolha a sua opção''')
        print()
        op = input('Digite aqui: ')
        if op == '1':
            novo()
        elif op == '2':
            mostraEmails()
        elif op == '3':
            print('Cadastro Encerrado')
            break
        else:
            print('Opção Inválida.')

main()