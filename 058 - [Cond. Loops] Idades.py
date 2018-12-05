#058 - Entrar com a idade de várias pessoas e imprimir:
#Total de pessoas com menos de 21 anos;
#Total de pessoas com mais de 50 anos.
 
#1 - Crie duas listas, sendo uma para pessoas menores de 21 anos e outra para maiores de 50 anos.
menoresde21 = []
maioresde50 = []
 
#2 - Crie um looping para digitar as idades até que a palavra 'fim' seja digitada.
fim = 'n'
while fim == 'n' :
    idade = int(input('Digite a sua idade: '))
    if idade < 21:
        menoresde21.append(idade)
    elif idade > 50:
        maioresde50.append(idade)
    else:
        print('Somente pessoas menores de 21 anos e maiores de 50 anos podem realizar cadastro.')
        print('Você deseja continuar digitando?(Digite s-Sim ou n-Não): ')
        fim = input('Digite a sua resposta: ').lower()
        if fim == 's':
            break
 
#3 - Faça a contagem das listas.
menoresDe21 = len(menoresde21)
maioresDe50 = len(maioresde50)
 
#4 - Imprima os resultados.
print('A quantidade de pessoas menores de 21 anos é', menoresDe21)
print('A quantidade de pessoas maiores de 50 anos é', maioresDe50)