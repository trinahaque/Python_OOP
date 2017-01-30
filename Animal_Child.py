from animal import Animal

class Dog(Animal):

    def __init__(self,name):
        self.health = 150
        self.name = name

    # def heal(self):
    #     self.health = 150
    #     return self

    def pet(self):
        self.health = self.health + 5
        return self

    def displayHealth(self):
        print "This is dog"
        return self

        # return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name, 170)
        # self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def displayInfo(self):
        print "This is dragon"
        super(Dragon, self).displayInfo()


# dog = Dog('Dog')
# #dog.heal().walk().run().pet().displayInfo()
# dog.walk().run().pet().displayHealth().displayInfo()
newDragon = Dragon("dragon")
newDragon.fly().run().displayInfo()

# dragon = Animal("Dragon")
# dragon.Dragon().displayInfo()
# dragon.walk().walk().fly().run().fly().displayInfo()
