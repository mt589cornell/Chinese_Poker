class Hand:
    ranks = ["Empty",
             "Single",
             "Double",
             "Straight",
             "Flush",
             "House",
             "Four",
             "Straight Flush",
             "Royal Flush"]

    def __init__(self, cards=[]):
       self.cards = cards


    def __rank__(self):
        # return hand rank
        if len(self.cards) == 0:
            return self.ranks[0]
        if len(self.cards) == 1:
           return self.ranks[1]
        if len(self.cards) == 2:
           return self.ranks[2]
        if len(self.cards) == 5:
           return self.five_type()

    def __size__(self):
        # return hand size
        return len(self.cards)

    def five_type(self):
        self.sort_by_value()

        values = [card.value for card in self.cards]
        suits = [card.suit for card in self.cards]

        # determine straights and flushes
        straight = (values == list(range(min(values), max(values)+1)))
        flush = all(s == suits[0] for s in suits)
        royal = (values == [10, 11, 12, 13, 14])

        if straight and flush:
            if royal:
                return self.ranks[8]
            return self.ranks[7]
        elif straight:
            return self.ranks[3]
        elif flush:
            return self.ranks[4]

        # determine if house or four-of-kind
        for v in set(values):
            if values.count(v) == 4:
                return self.ranks[6]
            if values.count(v) == 3:
                remaining = set(values).difference([v])
                for v2 in remaining:
                    if values.count(v2) == 2:
                        return self.ranks[5]


    def compare(self, opp_hand: 'Hand'):
        rank1 = self.__rank__()
        rank2 = opp_hand.__rank__()

        if self.ranks.index(rank1) > self.ranks.index(rank2):
            return 1
        elif self.ranks.index(rank1) < self.ranks.index(rank2):
            return 2
        else:
            return self.tie_breaker(opp_hand)

    def tie_breaker(self, opp_hand: 'Hand'):
        self.sort_by_value()
        opp_hand.sort_by_value()

        values = [card.value for card in self.cards]
        suits = [card.suit for card in self.cards]
        opp_values = [card.value for card in opp_hand.cards]
        opp_suits = [card.suit for card in opp_hand.cards]

        if self.__rank__() == "Single":
            if self.cards[0].value == opp_hand.cards[0].value:
                if self.cards[0].suit > opp_hand.cards[0].suit:
                    return 1
                else:
                    return 2
            elif self.cards[0].value > opp_hand.cards[0].value:
                return 1
            else:
                return 2

        if self.__rank__() == "Double":
            if self.cards[0].value == opp_hand.cards[0].value:
                if max(suits) > max(opp_suits):
                    return 1
                else:
                    return 2
            elif self.cards[0].value > opp_hand.cards[0].value:
                return 1
            else:
                return 2

        if self.__rank__() == "Straight":
            if self.cards[4].value == opp_hand.cards[4].value:
                if self.cards[4].suit > opp_hand.cards[4].suit:
                    return 1
                else:
                    return 2
            elif self.cards[4].value > opp_hand.cards[4].value:
                return 1
            else:
                return 2

        if self.__rank__() == "Flush":
            if self.cards[4].suit == opp_hand.cards[4].suit:
                if self.cards[4].value > opp_hand.cards[4].value:
                    return 1
                else:
                    return 2
            elif self.cards[4].suit > opp_hand.cards[4].suit:
                return 1
            else:
                return 2

        if self.__rank__() == "House":

            trip = None
            double = None
            opp_trip = None
            opp_double = None

            for v in set(values):
                if values.count(v) == 3:
                    trip = v
                if values.count(v) == 2:
                    double = v

            for v in set(opp_values):
                if opp_values.count(v) == 3:
                    opp_trip = v
                if opp_values.count(v) == 2:
                    opp_double = v

            double_max_suit = max([card.suit for card in self.cards if card.value == double])
            opp_double_max_suit = max([card.suit for card in opp_hand.cards if card.value == opp_double])

            if trip == opp_trip:
                if double == opp_double:
                    if double_max_suit > opp_double_max_suit:
                        return 1
                    else:
                        return 2
                elif double > opp_double:
                    return 1
                else:
                    return 2
            elif trip > opp_trip:
                return 1
            else:
                return 2


        if self.__rank__() == "Four":

            four = None
            single = None
            opp_four = None
            opp_single = None

            for v in set(values):
                if values.count(v) == 4:
                    four = v
                if values.count(v) == 1:
                    single = v

            for v in set(opp_values):
                if opp_values.count(v) == 4:
                    opp_four = v
                if opp_values.count(v) == 1:
                    opp_single = v

            single_max_suit = max([card.suit for card in self.cards if card.value == single])
            opp_single_max_suit = max([card.suit for card in opp_hand.cards if card.value == opp_single])

            if four == opp_four:
                if single == opp_single:
                    if single_max_suit > opp_single_max_suit:
                        return 1
                    else:
                        return 2
                elif single > opp_single:
                    return 1
                else:
                    return 2
            elif four > opp_four:
                return 1
            else:
                return 2

        if self.__rank__() == "Straight Flush" or self.__rank__() == "Royal Flush":

            suit = self.cards[0].suit
            max_val = self.cards[4].value
            opp_suit = opp_hand.cards[0].suit
            opp_max_val = opp_hand.cards[4].value

            if suit == opp_suit:
                if max_val > opp_max_val:
                    return 1
                else:
                    return 2
            elif suit > opp_suit:
                return 1
            else:
                return 2


    def sort_by_value(self):
        # sort hand
        self.cards.sort(key=lambda card: card.value)

    def __display__(self):
        hand = ""
        for card in self.cards:
            hand = hand + ", " + card.__repr__()
        print(hand)

    def __repr__(self):
        hand = ""
        for card in self.cards:
            hand = hand + ", " + card.__repr__()
        return hand
