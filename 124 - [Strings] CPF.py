#124 - Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx 
#e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.

cpf = input('Digite o seu cpf no formato xxx.xxx.xxx-xx: ')
tamCPF = len(cpf)
if tamCPF == 14 and '.' in cpf[3] and '.' in cpf[7] and '-' in cpf[11]:
    print('{} é um CPF válido'.format(cpf))
else:
    print('{} é um CPF inválido.'.format(cpf))