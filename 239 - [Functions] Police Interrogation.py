#244 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#a. "Telefonou para a vítima?"
#b. "Esteve no local do crime?"
#c. "Mora perto da vítima?"
#d. "Devia para a vítima?"
#e. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a
#participação
#da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser
#classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
#Caso contrário, ele será classificado como "Inocente".

def Questions():
    questions = ['Did you call the victim?', 
    'Were you at the crime scene?', 'Do you live near the victim?', 
    'Did you owe the victim?','Have you worked with the victim?']

    score = 0

    status = {1: 'Innocent', 2:'Suspect', 3:'Accomplice', 4:'Accomplice', 5:'Guilty'}

    data_input = 'Y or N?: '

    for index in range(len(questions)):
        print()
        print(questions[index])
        print()
        answer = input(data_input).upper()
        if answer == 'Y':
            score += 1
    
    if score in status:
        print(f'You Are {status[score]}')
    else:
        if score == 0:
            print('You Are Innocent')

def main():
    print()
    again = 'Y'
    while again == 'Y':
        print()
        print('Do You Want to Start the Interrogation? Y or N')
        opt = input('Answer: ').upper()
        if opt == 'Y':
            Questions()
        elif opt == 'N':
            print('Shutdown!')
            break
        
        print()
        print('Do you want to try again? Y or N')
        again = input('Option: ').upper()
        if again == 'N':
            print('Turn Off!')
            exit()
    else:
        print('Invalid Answer!')

main()