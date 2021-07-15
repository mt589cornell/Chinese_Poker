import unittest
from Game import Game

class MyTestCase(unittest.TestCase):
    def test_deal(self):
        game = Game()
        game.deal_cards(13)

        player_1 = game.p1
        player_2 = game.p2
        deck = game.deck
        print(player_1.name)
        print(player_1.num_cards())
        print(deck.remaining_cards())
        self.assertEqual(player_1.num_cards(), 13)
        self.assertEqual(player_2.num_cards(), 13)
        self.assertEqual(deck.remaining_cards(), 26)

    def test_deck_out(self):
        game = Game()
        game.deal_cards(26)

        player_1 = game.p1
        player_2 = game.p2
        deck = game.deck

        # no cards left to draw
        print(deck.remaining_cards())
        try:
            player_1.draw(deck)
        except ValueError as err:
            print(err)

    def test_pass(self):
        game = Game()
        game.deal_cards(5)

        player_1 = game.p1
        player_2 = game.p2
        deck = game.deck
        print(player_1.name)
        print(player_1.num_cards())
        player_1.__display__()
        print(deck.remaining_cards())

        game.pass_or_play(player_1, "pass")
        print(player_1.num_cards())
        player_1.__display__()

        self.assertEqual(player_1.num_cards(), 6)
        self.assertEqual(player_2.num_cards(), 5)
        self.assertEqual(deck.remaining_cards(), 41)

    def test_hand_gen(self):
        game = Game()
        game.deal_cards(5)

        player_1 = game.p1
        player_2 = game.p2
        deck = game.deck
        print(player_1.name)
        print(player_1.num_cards())
        player_1.__display__()


        game.pass_or_play(player_1, "1,3")
        print(player_1.num_cards())
        player_1.__display__()

        self.assertEqual(player_1.num_cards(), 3)
        self.assertEqual(player_2.num_cards(), 5)
        self.assertEqual(deck.remaining_cards(), 42)

    def test_winner(self):
        game = Game()
        game.deal_cards(5)

        player_1 = game.p1
        player_2 = game.p2
        deck = game.deck
        print(player_1.name)
        print(player_1.num_cards())
        player_1.__display__()


        game.pass_or_play(player_1, "0,1,2,3,4")
        print(player_1.num_cards())
        player_1.__display__()

        game.check_winner(player_1)

        self.assertEqual(player_1.num_cards(), 0)
        self.assertEqual(player_2.num_cards(), 5)
        self.assertEqual(deck.remaining_cards(), 42)
        self.assertEqual(game.active, False)

    def test_game(self):
        game = Game()

        player_1 = game.p1
        player_2 = game.p2
        deck = game.deck

        game.play_game()

        self.assertEqual(player_1.num_cards(), 13)
        self.assertEqual(player_2.num_cards(), 13)
        self.assertEqual(deck.remaining_cards(), 26)


if __name__ == '__main__':
    unittest.main()
