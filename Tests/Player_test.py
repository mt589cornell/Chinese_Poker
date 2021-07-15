import unittest
from Deck import Deck
from Player import Player

class MyTestCase(unittest.TestCase):
    def test_creation(self):
        player = Player('dummy')
        self.assertEqual(player.name, 'dummy')
        self.assertEqual(player.wins, 0)
        self.assertEqual(player.curr, [])

    def test_draw(self):
        deck = Deck()
        player = Player('dummy')

        player.draw(deck)
        player.__display__()
        self.assertEqual(player.name, 'dummy')
        self.assertEqual(player.wins, 0)
        self.assertEqual(len(player.curr), 1)
        self.assertEqual(deck.remaining_cards(), 51)

    def test_draw52(self):
        deck = Deck()
        player = Player('dummy')

        for i in range(52):
            player.draw(deck)

        self.assertEqual(player.name, 'dummy')
        self.assertEqual(player.wins, 0)
        self.assertEqual(len(player.curr), 52)
        self.assertEqual(deck.remaining_cards(), 0)

    def test_draw5(self):
        deck = Deck()
        player = Player('dummy')

        for i in range(5):
            player.draw(deck)

        player.sort_by_value()

        self.assertEqual(player.name, 'dummy')
        self.assertEqual(player.wins, 0)
        self.assertEqual(len(player.curr), 5)
        print(player.curr[0].value, player.curr[-1].value)
        self.assertLessEqual(player.curr[0].value, player.curr[-1].value)

if __name__ == '__main__':
    unittest.main()
