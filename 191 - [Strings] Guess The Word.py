import random

arq = open(input('File: '), 'r')
words = arq.readlines()
arq.close()
word = []

for i in words:
    word.append(i.strip())


sortedWord = random.choice(word)

letters = []
correct = []
lives = 6

while True:
    password = ''
    for let in sortedWord:
        password += let if let in correct else '.'
    print('Password: 'f'{password}')
    if password == sortedWord:
        print('Congratulations! You Win!')
        break
    chance = input('Letter: ').lower().strip()
    if chance in letters:
        print('This letter has already used')
        continue
    else:
        letters += chance
        if chance in sortedWord:
            correct += chance
        else:
            lives -= 1
            print('Wrong letter. Chances left: 'f'{lives}')
    if lives == 0:
        print('You lose. The right answer is 'f'{sortedWord}')
        break