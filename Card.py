import pygame

class Card:
    suits = ["diamonds",
             "clubs",
             "hearts",
             "spades"]

    values = [None, None, None, "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace", "2"]

    def __init__(self, v, s):
        """suit + value are ints"""
        self.value = v
        self.suit = s
        self.text = self.__repr__()
        self.x = None
        self.y = None
        self.color = (255, 255, 255)
        self.width = None
        self.height = None
        self.selected = False

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + \
            " of " + \
            self.suits[self.suit]
        return v

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 20)
        text = font.render(self.text, 1, (0,0,0))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False
