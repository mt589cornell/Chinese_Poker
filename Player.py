from Deck import Deck
from Hand import Hand

class Player:
    def __init__(self, name):
       self.wins = 0
       self.curr = []
       self.name = name
       self.turn = False

    def draw(self, deck: 'Deck'):
        card = deck.draw()
        self.curr.append(card)

    def num_cards(self):
        return len(self.curr)

    def sort_by_value(self):
        # sort hand
        self.curr.sort(key=lambda card: card.value)

    def get_lowest_card(self):
        self.sort_by_value()
        return self.curr[0]

    def __display__(self):
        self.sort_by_value()
        hand = []
        for card in self.curr:
            hand.append(card.__repr__())
        print("Player {} cards".format(self.name))
        print(hand)

    def update_win_state(self):
        if len(self.curr) == 0:
            self.wins = 1

    def play_cards(self, selection: []):
        choice = []
        selection.sort()
        selection.reverse()
        for select in selection:
            choice.append(self.curr.pop(select))
        choice.reverse()

        return Hand(choice)