from random import shuffle
from Card import Card
import pygame


class Deck:
    def __init__(self):
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        self.color = (0, 0, 0)
        self.cards = []
        for i in range(3, 16):
            for j in range(4):
                self.cards\
                    .append(Card(i,
                                 j))
        shuffle(self.cards)
        self.text = str(self.remaining_cards())


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

    def draw_deck(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 20)
        text = font.render(self.text, 1, (255,255,255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))
