import pygame
from networking.network import Network
import pickle
pygame.font.init()

width = 700
height = 700
# opens GUI window
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")



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

        # check who's turn it is
        if game.players[player].turn:
            print("Your cards:")
            print(game.players[player].__display__())
            option = input("Enter your move: ")
            print(option)
            n.send(option)
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
