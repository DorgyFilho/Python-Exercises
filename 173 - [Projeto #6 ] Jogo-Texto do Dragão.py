import random
import time

def intro():
    print('''You are a brave adventurer to face this challenge. The legend of the twin dragons lasts to the present day.
Everyone who entered their castle perished tragically. This enclosure holds two rooms. One of them will lead you to glory.
Already the other will lead you to the despair of hell. In one of the rooms, there is a gentle dragon waiting for you to find the treasure
to destroy the curse of this castle. In the other room is the one responsible for not allowing those who have tried to find
the treasure would see the light again. In this room, there is the evil dragon, responsible for this curse to endure until today. You have the chance.
of your life. You can leave this castle in a consecrating way or it will rot in the bowels of hell. It's your choice. There is no turning back.
Good luck, because you will need it.''')
    print()

def chooseYourDestiny():
    choose = ''
    while choose not in ['1', '2']:
        print('Choose Your Destiny - 1 or 2: ')
        print()
        choose = input('Choose Your Option: ')
        print()
    return choose

def result(choose):
    print('You have chosen your destination.')
    time.sleep(3)
    print()
    print('Walk to the room you have chosen.')
    time.sleep(3)
    print()
    print('Now there is no turning back.')
    time.sleep(3)
    print()
    print('Behold, the great dragon appears.')
    time.sleep(3)
    print()
    print('And now you ...')
    time.sleep(3)
    print()

    option = random.randint(1, 2)

    if choose == str(option):
        print('... will receive all the glories because you won the treasure and broke the curse of the castle!!!')
    else:
        print('... will perish in the darkest hell! HAHAHAHAHAHAHA !!!')

again = 'Y'
while again == 'Y':
    print()
    intro()
    print()
    opt = chooseYourDestiny()
    print()
    result(opt)
    print()
    print('Do you want to try again? Y ou N')
    again = input('Choose Your Option: ').upper()
    if again == 'N':
        print('End of the game. Thank you and come back!')
        break
