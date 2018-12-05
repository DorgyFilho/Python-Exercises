#170 - Exercício 9.27 [Adaptado] - Nilo Menezes: Página 200
#Não utilizarei arquivos.

agenda = []

def pede_nome(padrao=''):
    nome = input('Nome: ')
    if nome == '':
        nome = padrao
    return (nome)

def pede_telefone(padrao=''):
    tel = input('Telefone: ')
    if tel == '':
        tel = padrao
    return tel

def pede_email(padrao=''):
    email = input('E-mail: ')
    if email == '':
        email = padrao
    return (email)

def mostra(nome, tel, email):
    print('Nome:{}\nTelefone:{}\nE-mail:{}'.format(nome,tel,email))

def pesquisa(nome):
    pesq = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == pesq:
            return p
    return None

def novo():
    global agenda, alterada
    nome = pede_nome()
    if pesquisa(nome) != None:
        print('Nome cadastrado.')
        return
    tel = pede_telefone()
    email = pede_email()
    agenda.append([nome, tel, email])
    alterada = True

def confirma(opcao):
    while True:
        opcao = input('Digite S para Sim ou N para não: {}'.format(opcao)).upper()
        if opcao in 'SN':
            return opcao
        else:
            print('Entrada inválida. Digite S ou N.')

def apaga():
    global agenda, alterada
    nome = pede_nome()
    pes = pesquisa(pede_nome())
    if p != None:
        if confirma('Deleção') == 'S':
            del agenda[pes]
            alterada = True
    else:
        print('Nome não encontrado.')

def altera():
    global alterada
    pes = pesquisa(pede_nome())
    if pes != None:
        nome = agenda[pes][0]
        tel = agenda[pes][1]
        email = agenda[pes][2]
        print('Contato Localizado')
        mostra(nome, tel, email)
        nome = pede_nome(nome)
        tel = pede_telefone(tel)
        email = pede_email(email)
        if confirma('Alterar') == 'S':
            agenda[pes] = [nome, tel, email]
            alterada = True
    else:
        print('Nome não encontrado.')

def lista():
    print('{:50}'.format('AGENDA'))
    print('='*50)
    for a,b in enumerate(agenda):
        print('Posições:')
        mostra(b[0], b[1], b[2])
    print('='*50)

def menu():
    while True:
        print('Agenda Telefônica: Escolha as seguintes opções:\n0-Sair\n1-Adicionar\n2-Alterar\n3-Apagar\n4-Lista')
        op = input('Digite sua opção aqui: ')
        if op == '0':
            print('Programa Encerrado.')
            break
        elif op == '1':
            novo()
        elif op == '2':
            altera()
        elif op == '3':
            apaga()
        elif op == '4':
            lista()

menu()




