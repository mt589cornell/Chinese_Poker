import socket
import pickle

PACKET_SIZE = 2048 * 4

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "25.9.252.98"
        self.port = 25565
        self.addr = (self.server, self.port)
        self.player = self.connect()


    def getPlayer(self):
        return self.player

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(PACKET_SIZE).decode() # works for strings
            # return pickle.loads(self.client.recv(2048).decode()) # works for objects
        except:
            pass

    def send(self, data):
        try:
            # self.client.send(pickle.dumps(data)) # works for objects
            self.client.send(str.encode(data)) # works for strings
            return pickle.loads(self.client.recv(PACKET_SIZE)) # works for objects
            # return self.client.recv(2048 * 2).decode()  # works for strings
        except socket.error as e:
            print(e)