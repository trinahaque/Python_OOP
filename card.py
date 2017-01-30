import random
class Card(object):
    def __init__(self, val, suite):
        self.val = val
        self.suite = suite

    def show(self):
        print self.val, self.suite
        return self
#card = Card('bob', 5)
#card.show()
#card.val

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
    def build(self):
        suites = ["spade", "heart", "clubs", "diamond"]
        for suite in suites:
            for i in range(1,14):
                #print suite, val
                self.cards.append(Card[suite, i])

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self, n=3):
        for s in range(n):
            for i in range(len(self.cards)-1, 0, -1):
           # print i
                randIdx = random.randint(0,i)
                if i == randIdx:
                    continue

              # print i , randIdx
               #print "same"
                 self.cards[i], self.cards[randi] = self.cards[randi], self.cards[i]
            
    def deal(self):
        self.cards.pop()
        
class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck, num =1):
        for i in range(num):
            self.hand.append(deck, deal())

    def showHand(self):
        for card in show.hand:
            
        
                
new_deck = Deck()
#new_deck.show()
deck.shuffle()

'''
    def deal(self):
         pass
     def shuffle(self):
         pass
     def show(self):
         pass
        
    
class Player(object):
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def draw(self):
        pass
    def discard(self):
        pass
    def show(self):
        pass

        fisher yates shuffle        '''
    
