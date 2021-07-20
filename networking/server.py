import socket
from _thread import *
import pickle
from Game import Game

server = "192.168.1.219"
port = 25565
PACKET_SIZE = 2048*4

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0


def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(PACKET_SIZE).decode()

            if gameId in games:
                game = games[gameId]

                if not data:
                    print("Disconnected")
                    break
                else:
                    if data == "reset":
                        game.reset() # start a new game
                    elif data != "get":
                        game.play(p, data) # update game with current player's moves
                    # print('Received: ', reply)
                    # print('Sending: ', reply)
                    reply = game
                    conn.sendall(pickle.dumps(reply))
            else:
                break
        except:
            break

    print("Lost connection")

    try:
        del games[gameId]
        print("Closing game: ", gameId)
    except:
        pass

    idCount -= 1
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2
    if idCount % 2 == 1:
        games[gameId] = Game()
        games[gameId].initialize_game()
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1
        print("Second player has joined")


    start_new_thread(threaded_client, (conn, p, gameId))