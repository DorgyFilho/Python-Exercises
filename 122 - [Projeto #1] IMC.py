#IMC Calculator

def imc(peso, alt):
    imc = peso/(alt**2)
    return imc

def cond(sexo, peso, altura):
    cond = imc(peso, altura)

    if sex == 'M':
        if cond < 20:
            return 'Under Weight'
        elif 20 <= cond < 25:
            return 'Normal Weight'
        elif 25 <= cond < 30:
            return 'Overweight.'
        elif 30 <= cond < 40:
            return 'Obesity'
        else:
            return 'Morbid Obesity.'
    
    if sex == 'F':
        if cond < 19:
            return 'Under weight'
        elif 19 <= cond < 24:
            return 'Normal Weight'
        elif 24 <= cond < 29:
            return 'Overweight'
        elif 29 <= cond < 39:
            return 'Obesity'
        else:
            return 'Morbid Obesity'

vPeso = False
while vPeso == False:
    peso = input('Weight: ')
    try:
        peso = float(peso)
        if peso <= 0:
            print('Digite o seu peso acima de zero.')
        else:
            vPeso = True
    except:
        print('Digite apenas valores numéricos, utilizando "." em caso de necessidade.')

vAlt = False
while vAlt == False:
    alt = input('Height: ')
    try:
        alt = float(alt)
        if alt <= 0:
            print('Digite sua altura acima de zero.')
        else:
            vAlt = True
    except:
        print('Digite apenas valores numéricos, utilizando "." em caso de necessidade.')

sex = input('Sex: ').upper()
IMC = imc(peso, alt)
COND = cond(sex, peso, alt)
print('Sex: {}'.format(sex))
print('Weight: {:.2f} kg'.format(peso))
print('Height: {:.2f} m'.format(alt))
print('IMC: {:.2f}'.format(IMC))
print('Status: {}'.format(COND))
