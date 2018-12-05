#147 - Write a Python program to get a dictionary from an object's fields.

class Comp(object):
    def __init__(self):
        self.a = 'Dorgy'
        self.b = 'Cecilia'
        self.c = 'Shiro'
        self.d = 'Saulo'
    
COM = Comp()
print(COM.__dict__)