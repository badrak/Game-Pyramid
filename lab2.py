class Card(object):

    def __init__(self, rank, suit, isvisible = False):
        self.rank = rank
        self.suit = suit
        self.isvisible = isvisible


class Table:
    class Deck:
        def __init__(self, card):
            self.rank = range(1, 14)
            self.suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
            self.card = card
            deck = []
            for i in self.suit:
                for j in self.rank:
                    deck.append(card(j, i))

        def shuffled(self):
            import random
            random.shuffle(self)
