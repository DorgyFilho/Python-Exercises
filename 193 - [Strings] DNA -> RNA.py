DNA = 'AGCT'
RNA = ''
for let in DNA:
    if let == 'A':
        RNA += 'U'
    elif let == 'G':
        RNA += 'C'
    elif let == 'C':
        RNA += 'G'
    elif let == 'T':
        RNA += 'A'

print(RNA)