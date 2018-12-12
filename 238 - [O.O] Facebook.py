class Facebook:
    name = None
    age = None
    FriendsList = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def addFriend(self):
        newFriend = ''
        while newFriend != 'NOT':
            newFriend = input('New friend or Not to exit: ').upper()
            if newFriend == 'NOT':
                print('Turn off!')
                break
            else:                
                self.age = int(input('Your Age: '))
                self.FriendsList.append(newFriend)
        return self.FriendsList
    
    def isYourFriend(self):
        search = ''
        while search != 'NOT':
            search = input('Search: ').upper()
            if search == 'NOT':
                print('Shutdown!')
                break
            else:
                if search in self.FriendsList:
                    return True
                else:
                    return False

NAME = input('Name: ').upper()
AGE = int(input('Age: '))
NEW = Facebook(NAME, AGE)
NEW.addFriend()
print(NEW.isYourFriend())
    