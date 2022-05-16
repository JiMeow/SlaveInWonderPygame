from threading import *
import socket
import json
import time
import pickle
import pygame
import hashlib
import random
from player import Player

server = "25.34.159.172"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server, port))
s.listen(20)
print("Waiting for a connection, Server Started")

currentPlayer = {}
maxPlayers = 50

playerdata = {}
roomstate = {}

seed = {}


def threaded_client(conn, id):
    print(id, "connected")
    playerdata[id] = Player(
        id, (random.randint(0, 100) + 50*id % 155, random.randint(0, 100) + 50*id % 155, random.randint(0, 100) + 50*id % 155))
    # playerdata[id] = Player(id, (255, 255, 255))
    conn.send(pickle.dumps(playerdata[id]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(65536))
            playerdata[id] = data["player"]
            if playerdata[id].room not in roomstate:
                seed[playerdata[id].room] = random.randint(0, 100000)
                roomstate[playerdata[id].room] = False
            roomstate[playerdata[id].room] = max(
                roomstate[playerdata[id].room], data["gamestart"])
            if not data:
                print("Disconnected")
                break
            else:
                reply = {
                    "allplayer": playerdata,
                    "gamestart": roomstate[playerdata[id].room],
                    "seed": seed[playerdata[id].room]
                }
            conn.sendall(pickle.dumps(reply))
        except Exception as e:
            print(e)
            break
    print(id, "disconnected")
    playerdata.pop(id)
    currentPlayer[id] = 0
    conn.close()


def main():
    for i in range(1, maxPlayers+1):
        currentPlayer[i] = 0
    idx = 0
    while True:
        conn, addr = s.accept()
        for i in range(1, maxPlayers+1):
            if currentPlayer[i] == 0:
                currentPlayer[i] = 1
                idx = i
                break
        thread = Thread(target=threaded_client, args=(conn, idx))
        thread.start()


main()
