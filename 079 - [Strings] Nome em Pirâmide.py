#079 - Nome em formato de pirâmide.

nome = input('Digite seu nome: ').upper()

tam = len(nome)

for i in range(len(nome)):
    espaco = int((tam-i)/2)
    print(' '*espaco+nome[:i+1])