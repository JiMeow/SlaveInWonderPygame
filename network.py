import socket
import pickle

from player import Player
from card import Card
from setting import *


class Network:
    def __init__(self):
        """
        It creates a socket object.
        """
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server
        self.port = port
        self.addr = (self.server, self.port)

    def getInitData(self):
        """
        It connects to the database and returns the connection object
        :return: The return value is the result of the connect() method.
        """
        return self.connect()

    def disconnect(self):
        """
        The function disconnects the client from the server
        """
        self.client.close()

    def connect(self):
        """
        It connects to the server and returns the data that the server sends
        :return: The server is returning a list of all the files in the directory.
        """
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(65536))
        except Exception as e:
            print(e)

    def send(self, data):
        """
        It sends data to the server, and then waits for a response

        :param data: The data to send to the server
        :return: The return value is a list of tuples.
        """
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
