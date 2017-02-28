class Card(object):

    def __init__(self, rank, suit, isvisible = False):
        self.rank = rank
        self.suit = suit


class Table:
    class Deck:
        def __init__(self):
            self.rank = range(1, 14)
            self.suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
            deck = []
            for i in suit:
                for j in rank:
                    deck.append(card(j, i))

        def shuffled(self):
            import random
            random.shuffle(self)
