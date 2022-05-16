import socket
import pickle

from player import Player
from card import Card

server = "25.34.159.172"
port = 5555


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server
        self.port = port
        self.addr = (self.server, self.port)

    def getInitData(self):
        return self.connect()

    def disconnect(self):
        self.client.close()

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(65536))
        except Exception as e:
            print(e)

    def send(self, data):
        packet = []
        self.client.send(pickle.dumps(data))
        while True:
            try:
                packet.append(self.client.recv(65536))
                obj = pickle.loads(b"".join(packet))
                wait = False
            except pickle.UnpicklingError:
                wait = True

            if not wait:
                break
        return obj
