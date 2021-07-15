from random import shuffle
from Card import Card


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(3, 16):
            for j in range(4):
                self.cards\
                    .append(Card(i,
                                 j))
        shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            raise ValueError('No more cards! Pass or Play')
        return self.cards.pop()

    def remaining_cards(self):
        return len(self.cards)

    def __display__(self):
        deck = []
        for card in self.cards:
            deck.append(card.__repr__())
        print(deck)