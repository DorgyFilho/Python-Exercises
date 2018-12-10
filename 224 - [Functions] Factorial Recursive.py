#228 - Recursive Factorial

def recFact(n):
    if n <= 0 or n == 1:
        return 1
    else:
        return n*recFact(n-1)

n = int(input('Number: '))
print(recFact(n))