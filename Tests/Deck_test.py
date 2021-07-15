import unittest
from Deck import Deck

class MyTestCase(unittest.TestCase):
    def test_create(self):
        deck = Deck()
        self.assertEqual(deck.remaining_cards(), 52)

    def test_display(self):
        deck = Deck()
        deck.__display__()
        self.assertEqual(deck.remaining_cards(), 52)

    def test_draw(self):
        deck = Deck()
        card = deck.draw()
        print(card.__repr__())
        self.assertEqual(deck.remaining_cards(), 51)

    def test_draw52(self):
        deck = Deck()
        for i in range(52):
            deck.draw()
        self.assertEqual(deck.remaining_cards(), 0)

if __name__ == '__main__':
    unittest.main()
