#240 - Login and Senha

AuxList = []
LoginList = ''
Change = False

def YourLogin(login=''):
    Log = input('Login: ')
    if Log == '':
        Log = login
    return Log

def YourPassword(password=''):
    Pass = input('Password: ')
    if Pass == '':
        Pass = password
    return Pass

def Search(Login):
    search = Login
    for l, p in enumerate(LoginList):
        if p[0] == search:
            return l

def addLogin():
    global AuxList, LoginList, Change
    Login = YourLogin()
    if Login not in AuxList:
        PassWord = YourPassword()
        AuxList.extend([Login, PassWord])
        LoginList = [AuxList[i:i+2] for i in range(0, len(AuxList), 2)]
        print('Login registered')
        Change = True
    else:
        print('Login already registered in our system.')
        Change = False

def Confirm(op):
    while True:
        op = input('Do You Confirm The Change? Y or N: ').upper()
        if op in 'YN':
            return op
        else:
            print('Invalid Answer. Y or N')

def ChangeInfo():
    global Change
    search = Search(YourLogin())
    if search != None:
        Login = LoginList[search][0]
        password = LoginList[search][1]
        Password = YourPassword(password)
        if Confirm('Change') == 'Y':
            LoginList[search] = [Login, Password]
            Change = True
    else:
        print('Login Not Found')
        Change = False

def Show():
    global LoginList
    print(LoginList)

def main():
    again = 'Y'
    while again == 'Y':
        print()
        print('Welcome To Shop\nChoose Your Option\n1-Register\n2-Change\n3-Show List\n4-Exit')
        print()
        opt = input('Answer: ')
        if opt == '1':
            addLogin()
        elif opt == '2':
            ChangeInfo()
        elif opt == '3':
            Show()
        elif opt == '4':
            print('Leaving the server...')
            break
        else:
            print('Invalid Option!')
        
        print()
        print('Do You Want to Try Again? Y or N')
        print()
        again = input('Option: ').upper()
        if again == 'N':
            print('Turn Off')
            exit()
    else:
        print('Invalid option!!!')

main()
