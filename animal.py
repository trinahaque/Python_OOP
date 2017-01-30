import random
class Animal(object):
    # def __init__(self, name, health=100):
    def __init__(self, name, health):
        #health = 100 or self.health = 100 ==> better method
        self.name = name
        self.health = health

    def walk(self):
        self.health = self.health + 1
        return self

    def run(self):
        self.health = self.health - 5
        return self

    def displayInfo(self):
        print self.name, self.health



# bob = Animal("Bob")
# bob.walk().walk().walk().run().run().displayInfo()
