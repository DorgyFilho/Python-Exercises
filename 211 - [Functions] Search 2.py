def search(List, word):
    if word in List:
        return True
    else:
        return False

msg = 'File: '
arq = open(input(msg), 'r')
FileIn = arq.readlines()
arq.close()
List = []
for i in FileIn:
    List.append(i.strip())

msg2 = 'Search: '

again = 'Y'
while again == 'Y':
    word = input(msg2)
    print(search(List, word))
    print('\n')
    print('Do You Want to Try Again? Y or N')
    print('Choose Your Option')
    again = input('Option: ').upper()
    if again == 'N':
        print('Turn Off')
        break
else:
    print('Invalid Option.')