class CardGame(object):
    def __init__(self, suite, val):
        self.suite = suite
        self.val = val

    def show(self):
        print self.suite, self.val
        #return self

class Deck(object):
    def __init__(self):
        #self.cards = []
        self.build()


    def build(self):
        self.cards = []
        suites = ["spade", "heart", "clubs", "diamond"]
        vals = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        for suite in suites:
            #print suite
            for val in vals:
                self.cards.append(CardGame(suite, val))
                #print "*"*len(self.cards)
                #print self.cards[0]
                #return self

    def show(self):
        for card in self.cards:
            card.show()
            #print card.suite, card.val

    # def shuffle(self):
        # for i in range()




deck1 = Deck()
# deck1.build()
deck1.build()

# card1 = CardGame("spade", 13)
# card1.show()
