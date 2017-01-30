from human import Human
class Wizard(Human):
    def __init__(self):
        super(Wizard, self).__init__()   # use super to call the Human __init__ method
        self.intelligence = 10
        print self.intelligence          # every wizard starts off with 10 intelligence
    def heal(self):
        self.health += 10
        print self.health

harry=Wizard()
harry.heal()
