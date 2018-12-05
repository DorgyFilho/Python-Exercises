import random

def guess(arq):
    letter = []
    correct = []
    word = []
    lives = 6
    words = arq.readlines()
    arq.close()

    for i in words:
        word.append(i.strip())

    sortedWord = random.choice(word)

    while True:
        password = ''
        for let in sortedWord:
            password += let if let in correct else '.'
        print('Password: 'f'{password}')
        if password == sortedWord:
            print('Congratulations! You Win!')
            break
        chance = input('Letter: ').lower().strip()
        if chance in letter:
            print('This letter has already used.')
            continue
        else:
            letter += chance
            if chance in sortedWord:
                correct += chance
            else:
                lives -= 1
                print('Wrong letter. Lives left: 'f'{lives}')
        if lives == 0:
            print('You lose. The correct answer is 'f'{sortedWord}')
            break

#MAIN

arq = open(input('File: '), 'r')
guess(arq)
            
