import pygame
from networking.network import Network
import pickle
pygame.font.init()

width = 1000
height = 650
# opens GUI window
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, 1, (255,255,255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False

# Initilize all the game buttons
btns = [Button("Play", width/4, height/2, (0,0,0)), Button("Pass", width/2, height/2, (255,0,0))]


def draw_deck(deck, win):
    x, y = (width - width/4), height/2
    deck.x = x
    deck.y = y
    deck.text = str(deck.remaining_cards())

    deck.width = width/10
    deck.height = height/5

    deck.draw_deck(win)


def draw_player_hand(player, win):
    x, y = 50, (height-height/4)-10

    for card in player.curr:
        card.x = x
        card.y = y
        # card.color = (255, 255, 255)
        card.width = width/(len(player.curr)+3)
        card.height = height/4

        card.draw(win)
        x += card.width+10


def draw_opponent_player_hand(player, win):
    x, y = 50, 10

    for card in player.curr:
        card.x = x
        card.y = y
        card.text = ""
        card.color = (255, 255, 255)
        card.width = width / (len(player.curr) + 3)
        card.height = height / 4

        card.draw(win)
        x += card.width + 10


def redrawWindow(win, game, p):
    win.fill((128,128,128))

    if not game.ready:
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Waiting for Player...", 1, (255,0,0), True)
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    elif game.winner:
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Player {} has won".format(game.winner.name), 1, (255, 0, 0), True)
        win.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2))
    else:
        font = pygame.font.SysFont("comicsans", 30)

        if game.players[p].turn:
            text = font.render("Opponent Played: {}".format(game.field), 1, (0, 255, 255))
            win.blit(text, (width / 7, height / 3))
            # text = font.render("Your Move", 1, (0, 255,255))
            # win.blit(text, (width/2, height/3))
        else:
            text = font.render("Opponents Turn", 1, (0, 255, 255))
            win.blit(text, (width / 7, height / 3))

        for btn in btns:
            btn.draw(win)

        draw_deck(game.deck, win)
        draw_player_hand(game.players[p], win)
        draw_opponent_player_hand(game.players[(p+1)%2], win)

    pygame.display.update()



def main():
    run = True
    clock = pygame.time.Clock()

    n = Network()
    player = int(n.getPlayer())
    print("You are player:", player+1)

    while run:
        clock.tick(60)

        try:
            game = n.send("get")
        except:
            run = False
            print("Could not find game")
            break

        # check if there is a winner and close game/connection
        if game.winner:
            print("Player {} has won".format(game.winner.name))
            run = False
            pygame.quit()
            break
           
        # draw game screen
        redrawWindow(win, game, player)
          
        # check who's turn it is
        if game.players[player].turn:
            print("Your cards:")
            print(game.players[player].__display__())
            # option = input("Enter your move: ")
            # print(option)
            # n.send(option)

            # wait for player to make move
            selecting = True
            while selecting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()

                    # check what cards were clicked
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        for i in range(len(game.players[player].curr)):
                            card = game.players[player].curr[i]
                            if card.click(pos) and game.ready:
                                if card.selected:
                                    card.selected = False
                                    card.color = (255, 255, 255)
                                    redrawWindow(win, game, player)
                                else:
                                    card.selected = True
                                    card.color = (255, 255, 0)
                                    redrawWindow(win, game, player)



                    #check if button was clicked
                    button_pressed = None
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        for btn in btns:
                            if btn.click(pos) and game.connected():
                                selecting = False
                                button_pressed = btn

            if button_pressed.text == "Play":
                selection = []
                for i in range(len(game.players[player].curr)):
                    card = game.players[player].curr[i]
                    if card.selected:
                        selection.append(i)

                # send selection in readable format
                selection = [str(x) for x in selection]
                selection = ",".join(selection)
                n.send(selection)
            else:
                n.send("Pass")
        else:
            print("Opponent's turn...")
            print("Opponent has {} cards left".format(game.players[player].num_cards()))
            print("Your cards:")
            print(game.players[player].__display__())
            wait = True
            while wait:
                game = n.send("get")
                if game.players[player].turn:
                    wait = False

            print("Opponent played:")
            if game.field:
                print(game.field)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()




while True:
    main()
