#078 - Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

# F
# FU
# FUL
# FULA
# FULAN
# FULANO

nome = input('Digite seu nome: ').upper()
tam = len(nome)
for i in range(len(nome)):
    espaco = int((tam-1)//2)
    print(''*espaco+nome[:i+1])