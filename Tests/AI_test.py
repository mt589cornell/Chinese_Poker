import unittest
from AI_Player import AI_Player
from Deck import Deck
from Hand import Hand
from Card import Card

class MyTestCase(unittest.TestCase):
    def test_creation(self):
        player = AI_Player()
        self.assertEqual(player.name, 'AI')
        self.assertEqual(player.wins, 0)
        self.assertEqual(player.curr, [])

    def test_draw(self):
        deck = Deck()
        player = AI_Player()

        player.draw(deck)
        player.__display__()
        self.assertEqual(player.name, 'AI')
        self.assertEqual(player.wins, 0)
        self.assertEqual(len(player.curr), 1)
        self.assertEqual(deck.remaining_cards(), 51)

    def test_check_hands_single(self):
        deck = Deck()
        player = AI_Player()

        for i in range(5):
            player.draw(deck)

        player.__display__()

        hands = player.get_possible_hands("Single", 1)
        for hand in hands:
            hand.__display__()

        self.assertEqual(player.name, 'AI')
        self.assertEqual(player.wins, 0)
        self.assertEqual(len(player.curr), 5)
        self.assertEqual(deck.remaining_cards(), 47)
        self.assertEqual(len(hands), 5)

    def test_check_hands_double(self):
        deck = Deck()
        player = AI_Player()

        for i in range(13):
            player.draw(deck)

        player.__display__()

        hands = player.get_possible_hands("Double", 2)
        for hand in hands:
            hand.__display__()

        self.assertEqual(player.name, 'AI')
        self.assertEqual(player.wins, 0)
        self.assertEqual(len(player.curr), 13)
        self.assertEqual(deck.remaining_cards(), 39)


    def test_get_value_group(self):
        # check for single pairs
        deck = Deck()
        player = AI_Player()

        for i in range(13):
            player.draw(deck)

        player.__display__()

        group = player.get_value_group(0)
        for card in group:
            print(card.__repr__())

    def test_findsubsets(self):
        # check for single pairs
        deck = Deck()
        player = AI_Player()

        for i in range(13):
            player.draw(deck)

        player.__display__()

        group = player.get_value_group(0)
        subsets1 = player.findsubsets(group, 1)
        subsets2 = player.findsubsets(group, 2)
        print(group)
        print(subsets1)
        print(subsets2)

    def test_combos1(self):
        # check for single pairs
        deck = Deck()
        player = AI_Player()

        for i in range(13):
            player.draw(deck)

        player.__display__()

        hands = player.combos(1)
        for hand in hands:
            Hand(hand).__display__()


    def test_combos2(self):
        # check for double pairs
        deck = Deck()
        player = AI_Player()

        for i in range(10):
            player.draw(deck)

        player.__display__()

        hands = player.combos(2)
        for hand in hands:
            Hand(hand).__display__()

    def test_combos3(self):
        # check for triples pairs
        deck = Deck()
        player = AI_Player()

        for i in range(13):
            player.draw(deck)

        player.__display__()

        hands = player.combos(3)
        for hand in hands:
            Hand(hand).__display__()

    def test_combos4(self):
        # check for quad pairs
        deck = Deck()
        player = AI_Player()

        for i in range(26):
            player.draw(deck)

        player.__display__()

        hands = player.combos(4)
        for hand in hands:
            Hand(hand).__display__()

    def test_get_fivehands(self):
        deck = Deck()
        player = AI_Player()

        for i in range(13):
            player.draw(deck)

        player.__display__()

        hands = player.get_fivehands()
        for hand in hands:
            hand.__display__()

    def test_get_possible_hands(self):
        deck = Deck()
        player = AI_Player()

        for i in range(13):
            player.draw(deck)

        player.__display__()

        hands = player.get_possible_hands("Straight", 5)
        for hand in hands:
            Hand(hand).__display__()

    def test_get_all_5card_combos(self):
        deck = Deck()
        player = AI_Player()

        for i in range(6):
            player.draw(deck)

        player.__display__()

        hands = player.get_all_5card_combos()
        for hand in hands:
            Hand(hand).__display__()

    def test_get_straights(self):
        deck = Deck()
        player = AI_Player()

        for i in range(13):
            player.draw(deck)

        player.__display__()

        hands = player.get_all_5card_combos()
        flushes = player.get_straights(hands)
        for hand in flushes:
            hand.__display__()

    def test_get_flushes(self):
        deck = Deck()
        player = AI_Player()

        for i in range(13):
            player.draw(deck)

        player.__display__()

        hands = player.get_all_5card_combos()
        flushes = player.get_flushes(hands)
        for hand in flushes:
            hand.__display__()

    def test_get_houses(self):
        deck = Deck()
        player = AI_Player()

        for i in range(13):
            player.draw(deck)

        player.__display__()

        hands = player.get_all_5card_combos()
        houses = player.get_houses(hands)
        for hand in houses:
            hand.__display__()

    def test_get_fourofkinds(self):
        deck = Deck()
        player = AI_Player()

        for i in range(26):
            player.draw(deck)

        player.__display__()

        hands = player.get_all_5card_combos()
        fourofkinds = player.get_fourofkind(hands)
        for hand in fourofkinds:
            hand.__display__()

    def test_get_straightflush(self):
        deck = Deck()
        player = AI_Player()

        for i in range(36):
            player.draw(deck)

        player.__display__()

        hands = player.get_all_5card_combos()
        straightflushes = player.get_straightflush(hands)
        for hand in straightflushes:
            hand.__display__()

    def test_get_royalflush(self):
        deck = Deck()
        player = AI_Player()

        for i in range(52):
            player.draw(deck)

        player.__display__()

        hands = player.get_all_5card_combos()
        royalflushes = player.get_royalflush(hands)
        for hand in royalflushes:
            hand.__display__()

    def test_get_beatsopponent(self):
        deck = Deck()
        player = AI_Player()

        for i in range(13):
            player.draw(deck)

        player.__display__()

        opponent_hand = Hand([Card(3,3), Card(3,4)])
        rank = opponent_hand.__rank__()
        size = opponent_hand.

        possible_hands = player.get_possible_hands()
        hands = player.beats_opponent(opponent_hand)
        royalflushes = player.get_royalflush(hands)
        for hand in royalflushes:
            hand.__display__()

if __name__ == '__main__':
    unittest.main()
