from Deck import Deck
from Player import Player
from AI_Player import AI_Player
from Hand import Hand

NUM_CARDS = 13

class Game:
    def __init__(self):
        # name1 = input("p1 name ")
        # name2 = input("p2 name ")
        # self.p1 = Player(name1)
        # self.p2 = Player(name2)
        self.deck = Deck()
        self.p1 = Player("p1")
        self.p2 = Player("p2")
        # self.p2 = AI_Player()
        self.ready = False
        self.players = [self.p1, self.p2]
        self.field = "pass"
        self.winner = None

    def connected(self):
        return self.ready

    def reset(self):
        self.deck = Deck()
        self.p1 = Player(self.p1.name)
        self.p2 = Player(self.p2.name)
        self.ready = True
        self.winner = None
        self.initialize_game()

    def deal_cards(self, num_cards):
        for i in range(num_cards):
            self.p1.draw(self.deck)
            self.p2.draw(self.deck)

    def initialize_game(self):
        print("Dealing {} cards each".format(NUM_CARDS))
        self.deal_cards(NUM_CARDS)

        p1_lowest_card = self.p1.get_lowest_card()
        p2_lowest_card = self.p2.get_lowest_card()

        if p1_lowest_card.value <= p2_lowest_card.value:
            first = self.p1.name
            self.p1.turn = True
        else:
            first = self.p2.name
            self.p2.turn = True

        # player one starts game
        print("Player {} goes first".format(first))

    def wins(self, winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)

    def check_winner(self, player: 'Player'):
        if player.num_cards() == 0:
            self.ready = False
            self.wins(player.name)
            self.winner = player

    def pass_or_play(self, player: 'Player', move) -> Hand:

        if move == "Pass":
            # draw a card
            try:
                player.draw(self.deck)
                print('Player {} has passed'.format(player.name))
                self.field = "Pass"
                return Hand([])
            except ValueError as err:
                print("No more cards in deck!, Player {} has passed".format(player.name))
            # update player turns
        else:
            # remove cards from player and create hand
            selection = move.split(",")
            selection = list(map(int, selection))
            field = player.play_cards(selection)
            self.field = field

            self.check_winner(player)

            return field



    def play(self, player, data):
        print("Player {} made a move".format(player))
        self.pass_or_play(self.players[player], data)
        self.players[player].turn = False
        opponent = (player + 1)%2
        self.players[opponent].turn = True


    def play_game(self):
        print("Dealing {} cards each".format(NUM_CARDS))
        self.deal_cards(NUM_CARDS)

        # player one starts game
        print("Player {} goes first".format(self.p1.name))

        while self.active:
            # display player hand
            self.p1.__display__()

            # player plays or pass
            move = input("Play cards or pass ")
            hand = self.pass_or_play(self.p1, move)

            # check player hand for game termination
            self.check_winner(self.p1)

            # opponent makes move
            move = self.p2.decision(opponent_hand=hand)
            hand = self.pass_or_play(self.p2, move)

            # check AI_player hand for game termination
            self.check_winner(self.p2)

        print("Game has ended!")