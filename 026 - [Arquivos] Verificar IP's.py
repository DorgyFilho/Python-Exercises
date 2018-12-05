#026 - Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere 
# um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
# O arquivo de entrada possui o seguinte formato:
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 257.32.4.5
# 85.345.1.2
# 1.2.3.4
# 9.8.234.5
# 192.168.0.256

# O arquivo de saída possui o seguinte formato:
# [Endereços válidos:]
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 1.2.3.4

# [Endereços inválidos:]
# 257.32.4.5
# 85.345.1.2
# 9.8.234.5
# 192.168.0.256

arq = open('/home/dorginho/ip.txt','r')
entrada = arq.readlines()
arq.close()

validos = ''
invalidos = ''

for i in range(len(entrada)):
    ip = entrada[i].split('.')
    if int(ip[0]) <= 254 and int(ip[1]) <= 254 and int(ip[2]) <= 254 and int(ip[3]) <= 254:
        validos += entrada[i] + '\n'
    else:
        invalidos += entrada[i] + '\n'

val = open('/home/dorginho/ipValido.txt', 'w')
inv = open('/home/dorginho/ipInvalido.txt', 'w')
val.write('[IPs VÁLIDOS]:' + '\n')
val.writelines(validos)
inv.write('[IPs INVÁLIDOS]:' + '\n')
inv.writelines(invalidos)
val.close()
inv.close()