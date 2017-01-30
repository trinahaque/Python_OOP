class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print self.price, self.max_speed, self.miles

    def ride(self):
        self.miles = self.miles + 10
        #print "Riding", self.miles, "miles"
        return self

    def reverse(self):
        self.miles = self.miles - 5
        if self.miles < 0:
            self.miles = 0

        return self
        #print "Reverse", self.miles, "miles"


bike2 = Bike(50, '100mph')
bike2.ride().ride().reverse().displayInfo()

bike1 = Bike(200, "20mph")
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()
#bike1.reverse()

bike3 = Bike(100, "10mph")
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()
