class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12

    def displayInfo(self):
        print "price:", self.price
        print "speed:", self.speed
        print "fuel:", self.fuel
        print "mileage:", self.mileage
        print "tax:", self.tax
car1 = Car(2000, "35mph", "Full", "15mph")
car1.displayInfo()

car2 = Car(20000000, "35mph", "Empty", "15mpg")
car2.displayInfo()
