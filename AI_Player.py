from Deck import Deck
from Hand import Hand
from Player import Player
from itertools import combinations
import more_itertools as mit


class AI_Player(Player):

    def __init__(self):
        Player.__init__(self, "AI")

    def get_possible_hands(self, rank, size):
        hands = []
        self.sort_by_value()

        if len(self.curr) < size:
            hands.append(Hand())
            return hands

        if rank == "Single":
            return self.combos(1)

        if rank == "Double":
            return self.combos(2)

        if rank not in ["Single", "Double"]:
            return self.get_fivehands()

    def combos(self, num):
        """
        :param num: can be in range 1-4
        :return: all unique combination of same value cards for a given combo size
        """
        combos = []
        start = 0
        while start <= len(self.curr)-num:
            # get continuous set of same values
            group = self.get_value_group(start)

            # get all combinations of same value for combo size
            subsets = self.findsubsets(group, num)

            # add subsets to combos
            for sub in subsets:
                combos.append(sub)

            # move to start of next group
            start += len(group)

        return combos

    def get_value_group(self, start):
        # expand group to include all equal values
        group = [self.curr[start]]
        i = start + 1
        while i < len(self.curr)-1 and group[0].value == self.curr[i].value:
            group.append(self.curr[i])
            i += 1

        return group

    def findsubsets(self, group, num):
        return list((map(list, combinations(group, num))))

    def get_fivehands(self):

        all_five_combos = self.get_all_5card_combos()

        straights = self.get_straights(all_five_combos)
        flushes = self.get_flushes(all_five_combos)
        houses = self.get_houses(all_five_combos)
        four_of_a_kind = self.get_fourofkind(all_five_combos)
        straight_flushes = self.get_straightflush(all_five_combos)
        royal_flushes = self.get_royalflush(all_five_combos)

        return straights + flushes + houses + four_of_a_kind + straight_flushes + royal_flushes

    def get_all_5card_combos(self):
        five_cards = combinations(self.curr, 5)
        hands = [Hand(list(hand)) for hand in five_cards]

        return hands

    def get_straights(self, hands: [Hand]):
        straights = [hand for hand in hands if hand.five_type() == "Straight"]
        return straights

    def get_flushes(self, hands: [Hand]):
        flushes = [hand for hand in hands if hand.five_type() == "Flush"]
        return flushes

    def get_houses(self, hands: [Hand]):
        houses = [hand for hand in hands if hand.five_type() == "House"]
        return houses

    def get_fourofkind(self, hands: [Hand]):
        fourofkinds = [hand for hand in hands if hand.five_type() == "Four"]
        return fourofkinds

    def get_straightflush(self, hands: [Hand]):
        straight_flushes = [hand for hand in hands if hand.five_type() == "Straight Flush"]
        return straight_flushes

    def get_royalflush(self, hands: [Hand]):
        royal_flushes = [hand for hand in hands if hand.five_type() == "Royal Flush"]
        return royal_flushes

    def decision(self, opponent_hand):
        if not opponent_hand.cards:
            # AI gets freebee
            self.freebee()
        else:
            # AI has to beat player hand
            rank = opponent_hand.__rank__()
            size = opponent_hand.__size__()

            # generate all possible hands
            possible_hands = self.get_possible_hands(rank, size)

            # find hands that beat opponents hand
            winning_hands = self.beats_opponent(opponent_hand, possible_hands)

            if not winning_hands:
                return "pass"
            else:
                print("do not pass")
                return

            print("Pause here")
            return

    def freebee(self):
        """
        TODO: Determine strategy AI should employ when given a free turn
        :return:
        """
        return

    def beats_opponent(self, opponent_hand, possible_hands):
        winning_hands = []
        for hand in possible_hands:
            if hand.compare(opponent_hand) == 1:
                winning_hands.append(hand)

        return winning_hands
