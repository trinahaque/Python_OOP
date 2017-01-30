class MathDojo(object):
    def __init__(self):
        self.total = 0

    def add(self, *restOfArg):
        for each in restOfArg:
            if type(restOfArg) == list:
                for val in restOfArg:
                    self.total +=val
                print self.total
            # else:
            #     self.total += restOfArg



        # if type(self.num2) != int:
        #     for val in self.num2:
        #         self.total +=val
        # else:
        #     self.total += self.num2
        #
        # print self.total


mathdojo = MathDojo()
mathdojo.add([3,5,7,8])
