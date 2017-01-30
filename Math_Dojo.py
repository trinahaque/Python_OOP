class MathDojo(object):
    def __init__(self):
        pass
        # self.add()
        # self.subtract()
        # self.result = self.show()
        # self.num1 = num1

    def add(self, num1, num2=None):
        self.num1 = num1
        self.num2 = num2
        if num2 is None:
            self.total = self.num1
        else:
            self.total = self.num1 + self.num2
        return self

    def subtract(self, num1, num2=None):
        self.num1 = num1
        self.num2 = num2
        if num2 is None:
            self.sub = self.num1
        else:
            self.sub = self.num1 + self.num2
        return self


    def show(self):
        print self.total - self.sub
        #return self


mathdojo = MathDojo()
mathdojo.add(2).subtract(1,2).show()
