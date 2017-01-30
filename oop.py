#Practicing OOP
#January 17, 2017

class Human(object):
    #needs object whenever creating a new class in python
    pass

    def my_function(self):
        print "This is a message inside the class."

    def taunt(self):
        print "You want a piece of me?"
'''
novak = Human()
novak.taunt()

print novak
'''

class Point(object):
    def __init__(self):
        print "New human"

    def distance(self):
        return "Want to play tennis"
'''
novak = Point()
novak.distance()

print novak
'''
