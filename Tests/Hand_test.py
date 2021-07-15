import unittest
from Hand import Hand
from Card import Card


class MyTestCase(unittest.TestCase):
    def test_rank(self):
        """
        check hand ranking assignment is correct
        :return:
        """
        card1 = Card(2,1)
        card2 = Card(3,2)
        test_hand = Hand([card1])
        self.assertEqual(test_hand.__rank__(), "Single")
        test_hand = Hand([card1, card2])
        self.assertEqual(test_hand.__rank__(), "Double")

    def test_display(self):
        card1 = Card(2, 1)
        card2 = Card(3, 2)
        test_hand = Hand([card1])
        print(test_hand.__display__())
        test_hand = Hand([card1, card2])
        print(test_hand.__display__())

    def test_sort(self):
        """
        check if hand sorts by value
        :return:
        """
        card1 = Card(3, 1)
        card2 = Card(2, 2)
        test_hand = Hand([card1, card2])
        print("Unsorted Hand")
        print(test_hand.__display__())
        test_hand.sort_by_value()
        print("Sorted Hand")
        print(test_hand.__display__())

    def test_single(self):
        card1 = Card(2, 1)
        test_hand = Hand([card1])
        self.assertEqual(test_hand.__rank__(), "Single")

    def test_double(self):
        card1 = Card(2, 1)
        card2 = Card(2, 2)
        test_hand = Hand([card1, card2])
        self.assertEqual(test_hand.__rank__(), "Double")

    def test_straight(self):
        card1 = Card(2, 1)
        card2 = Card(3, 2)
        card3 = Card(4, 1)
        card4 = Card(5, 2)
        card5 = Card(6, 1)
        test_hand = Hand([card1, card2, card3, card4, card5])
        self.assertEqual(test_hand.__rank__(), "Straight")

    def test_flush(self):
        card1 = Card(2, 1)
        card2 = Card(3, 1)
        card3 = Card(4, 1)
        card4 = Card(8, 1)
        card5 = Card(7, 1)
        test_hand = Hand([card1, card2, card3, card4, card5])
        self.assertEqual(test_hand.__rank__(), "Flush")

    def test_house(self):
        card1 = Card(2, 1)
        card2 = Card(2, 2)
        card3 = Card(2, 3)
        card4 = Card(5, 2)
        card5 = Card(5, 1)
        test_hand = Hand([card1, card2, card3, card4, card5])
        self.assertEqual(test_hand.__rank__(), "House")

    def test_four_of_a_kind(self):
        card1 = Card(2, 1)
        card2 = Card(2, 2)
        card3 = Card(2, 3)
        card4 = Card(2, 4)
        card5 = Card(6, 1)
        test_hand = Hand([card1, card2, card3, card4, card5])
        self.assertEqual(test_hand.__rank__(), "Four")

    def test_straight_flush(self):
        card1 = Card(2, 1)
        card2 = Card(3, 1)
        card3 = Card(4, 1)
        card4 = Card(5, 1)
        card5 = Card(6, 1)
        test_hand = Hand([card1, card2, card3, card4, card5])
        self.assertEqual(test_hand.__rank__(), "Straight Flush")

    def test_royal_flush(self):
        card1 = Card(10, 1)
        card2 = Card(11, 1)
        card3 = Card(12, 1)
        card4 = Card(13, 1)
        card5 = Card(14, 1)
        test_hand = Hand([card1, card2, card3, card4, card5])
        self.assertEqual(test_hand.__rank__(), "Royal Flush")

    def test_compare_single(self):
        # player wins
        card1 = Card(11, 1)
        card2 = Card(10, 1)
        player_hand = Hand([card1])
        opp_hand = Hand([card2])
        result = player_hand.compare(opp_hand)
        self.assertEqual(result, 1)

        # opponent wins
        player_hand = Hand([card2])
        opp_hand = Hand([card1])
        result = player_hand.compare(opp_hand)
        self.assertEqual(result, 2)

        # same value, player wins by suit
        card1 = Card(10, 2)
        card2 = Card(10, 1)
        player_hand = Hand([card1])
        opp_hand = Hand([card2])
        result = player_hand.compare(opp_hand)
        self.assertEqual(result, 1)

        # same value, opponent wins by suit
        player_hand = Hand([card2])
        opp_hand = Hand([card1])
        result = player_hand.compare(opp_hand)
        self.assertEqual(result, 2)

    def test_compare_double(self):
        # player wins
        card1 = Card(10, 1)
        card2 = Card(10, 2)
        card3 = Card(5, 1)
        card4 = Card(5, 2)
        player_hand = Hand([card1, card2])
        opp_hand = Hand([card3, card4])
        result = player_hand.compare(opp_hand)
        self.assertEqual(result, 1)

        # opponent wins
        player_hand = Hand([card3, card4])
        opp_hand = Hand([card1, card2])
        result = player_hand.compare(opp_hand)
        self.assertEqual(result, 2)

        # same value, player wins by suit
        card1 = Card(10, 1)
        card2 = Card(10, 4)
        card3 = Card(10, 2)
        card4 = Card(10, 3)
        player_hand = Hand([card1, card2])
        opp_hand = Hand([card3, card4])
        result = player_hand.compare(opp_hand)
        self.assertEqual(result, 1)

        # same value, opponent wins by suit
        player_hand = Hand([card3, card4])
        opp_hand = Hand([card1, card2])
        result = player_hand.compare(opp_hand)
        self.assertEqual(result, 2)

    def test_compare_straight(self):
        # player wins
        card1 = Card(3, 1)
        card2 = Card(4, 2)
        card3 = Card(5, 1)
        card4 = Card(6, 2)
        card5 = Card(7, 2)

        card6 = Card(2, 1)
        card7 = Card(3, 2)
        card8 = Card(4, 1)
        card9 = Card(5, 2)
        card10 = Card(6, 2)
        player_hand = Hand([card1, card2, card3, card4, card5])
        opp_hand = Hand([card6, card7, card8, card9, card10])
        result = player_hand.compare(opp_hand)
        self.assertEqual(result, 1)

        # opponent wins
        player_hand = Hand([card6, card7, card8, card9, card10])
        opp_hand = Hand([card1, card2, card3, card4, card5])
        result = player_hand.compare(opp_hand)
        self.assertEqual(result, 2)

        # same value, player wins by suit
        card1 = Card(3, 1)
        card2 = Card(4, 2)
        card3 = Card(5, 1)
        card4 = Card(6, 2)
        card5 = Card(7, 4)

        card6 = Card(3, 1)
        card7 = Card(4, 2)
        card8 = Card(5, 1)
        card9 = Card(6, 2)
        card10 = Card(7, 2)
        player_hand = Hand([card1, card2, card3, card4, card5])
        opp_hand = Hand([card6, card7, card8, card9, card10])
        result = player_hand.compare(opp_hand)
        self.assertEqual(result, 1)

        # same value, opponent wins by suit
        player_hand = Hand([card6, card7, card8, card9, card10])
        opp_hand = Hand([card1, card2, card3, card4, card5])
        result = player_hand.compare(opp_hand)
        self.assertEqual(result, 2)

    def test_compare_flush(self):
        # player wins
        card1 = Card(4, 3)
        card2 = Card(8, 3)
        card3 = Card(2, 3)
        card4 = Card(9, 3)
        card5 = Card(5, 3)

        card6 = Card(4, 1)
        card7 = Card(8, 1)
        card8 = Card(2, 1)
        card9 = Card(9, 1)
        card10 = Card(5, 1)
        player_hand = Hand([card1, card2, card3, card4, card5])
        opp_hand = Hand([card6, card7, card8, card9, card10])
        result = player_hand.compare(opp_hand)
        self.assertEqual(result, 1)

        # opponent wins
        player_hand = Hand([card6, card7, card8, card9, card10])
        opp_hand = Hand([card1, card2, card3, card4, card5])
        result = player_hand.compare(opp_hand)
        self.assertEqual(result, 2)

        # same suit, player wins by value
        card1 = Card(4, 3)
        card2 = Card(8, 3)
        card3 = Card(2, 3)
        card4 = Card(12, 3)
        card5 = Card(5, 3)

        card6 = Card(4, 1)
        card7 = Card(8, 1)
        card8 = Card(2, 1)
        card9 = Card(9, 1)
        card10 = Card(5, 1)
        player_hand = Hand([card1, card2, card3, card4, card5])
        opp_hand = Hand([card6, card7, card8, card9, card10])
        result = player_hand.compare(opp_hand)
        self.assertEqual(result, 1)

        # same suit, opponent wins by value
        player_hand = Hand([card6, card7, card8, card9, card10])
        opp_hand = Hand([card1, card2, card3, card4, card5])
        result = player_hand.compare(opp_hand)
        self.assertEqual(result, 2)

    def test_compare_house(self):
        # player wins
        card1 = Card(8, 1)
        card2 = Card(8, 2)
        card3 = Card(8, 3)
        card4 = Card(10, 3)
        card5 = Card(10, 2)

        card6 = Card(4, 1)
        card7 = Card(4, 4)
        card8 = Card(4, 2)
        card9 = Card(5, 1)
        card10 = Card(5, 2)
        player_hand = Hand([card1, card2, card3, card4, card5])
        opp_hand = Hand([card6, card7, card8, card9, card10])
        result = player_hand.compare(opp_hand)
        self.assertEqual(result, 1)

        # opponent wins
        player_hand = Hand([card6, card7, card8, card9, card10])
        opp_hand = Hand([card1, card2, card3, card4, card5])
        result = player_hand.compare(opp_hand)
        self.assertEqual(result, 2)

    def test_compare_four(self):
        # player wins
        card1 = Card(8, 1)
        card2 = Card(8, 2)
        card3 = Card(8, 3)
        card4 = Card(8, 4)
        card5 = Card(10, 2)

        card6 = Card(4, 1)
        card7 = Card(4, 4)
        card8 = Card(4, 2)
        card9 = Card(4, 3)
        card10 = Card(5, 2)
        player_hand = Hand([card1, card2, card3, card4, card5])
        opp_hand = Hand([card6, card7, card8, card9, card10])
        result = player_hand.compare(opp_hand)
        self.assertEqual(result, 1)

        # opponent wins
        player_hand = Hand([card6, card7, card8, card9, card10])
        opp_hand = Hand([card1, card2, card3, card4, card5])
        result = player_hand.compare(opp_hand)
        self.assertEqual(result, 2)

    def test_compare_straight_royal_flush(self):
        # player wins
        card1 = Card(2, 2)
        card2 = Card(3, 2)
        card3 = Card(4, 2)
        card4 = Card(5, 2)
        card5 = Card(6, 2)

        card6 = Card(3, 1)
        card7 = Card(4, 1)
        card8 = Card(5, 1)
        card9 = Card(6, 1)
        card10 = Card(7, 1)

        player_hand = Hand([card1, card2, card3, card4, card5])
        opp_hand = Hand([card6, card7, card8, card9, card10])
        result = player_hand.compare(opp_hand)
        self.assertEqual(result, 1)

        # opponent wins
        player_hand = Hand([card6, card7, card8, card9, card10])
        opp_hand = Hand([card1, card2, card3, card4, card5])
        result = player_hand.compare(opp_hand)
        self.assertEqual(result, 2)

        # same value, player wins by suit
        card1 = Card(3, 3)
        card2 = Card(4, 3)
        card3 = Card(5, 3)
        card4 = Card(6, 3)
        card5 = Card(7, 3)

        card6 = Card(3, 1)
        card7 = Card(4, 1)
        card8 = Card(5, 1)
        card9 = Card(6, 1)
        card10 = Card(7, 1)
        player_hand = Hand([card1, card2, card3, card4, card5])
        opp_hand = Hand([card6, card7, card8, card9, card10])
        result = player_hand.compare(opp_hand)
        self.assertEqual(result, 1)

        # same value, opponent wins by suit
        player_hand = Hand([card6, card7, card8, card9, card10])
        opp_hand = Hand([card1, card2, card3, card4, card5])
        result = player_hand.compare(opp_hand)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
