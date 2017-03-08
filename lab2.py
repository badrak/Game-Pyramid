import random


class Card(object):
    def __init__(self, rank, suit, isvisible=False):
        self.rank = rank
        self.suit = suit
        self.isvisible = isvisible

    def __repr__(self):
        return"%s %s" % (self.suit, self.rank)


class Deck:
    def __init__(self):
        self.rank = range(1, 14)
        self.suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.deck = []
        for suit in self.suit:
            for rank in self.rank:
                self.deck.append(Card(rank, suit))
        random.shuffle(self.deck)

    def __str__(self):
        return self.deck

    def __next__(self):
        return self.deck.pop(0)


class Pyramid:
    def __init__(self):
        self.cards_pyramid = []

    def __str__(self):
        return self.cards_pyramid


class Game:
    def __init__(self):
        self.deck = Deck()
        self.pyramid = Pyramid()
        for i in range(28):
            self.pyramid.cards_pyramid.append(self.deck.__next__())

    def __str__(self):
        return self.pyramid.cards_pyramid

if __name__ == "__main__":
    my_deck = Deck()
    print('Полная колода - ', my_deck.__str__())
    my_game = Game()
    print('Колода пирамиды - ', my_game.__str__())
