from threading import *
import socket
import json
import time
import pickle
import pygame
import hashlib
import random

from table import Table
from player import Player

server = "25.34.159.172"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server, port))
s.listen(20)
print("Waiting for a connection, Server Started")

currentPlayer = {}
maxPlayers = 50

# key: id, value: class player
playerdata = {}

# key: room, value: boolean
roomstate = {}
# key: room, value: class Table
table = {}
# key: room, value: class player
turn = {}

# key: room, value: List[players] in the room
playerinroom = {}

seed = {}


def threaded_client(conn, id):
    print(id, "connected")
    playerdata[id] = Player(
        id, (random.randint(0, 100) + 50*id % 155, random.randint(0, 100) + 50*id % 155, random.randint(0, 100) + 50*id % 155))
    # playerdata[id] = Player(id, (255, 255, 255))
    conn.send(pickle.dumps(playerdata[id]))
    reply = ""
    while True:
        # try:
        data = pickle.loads(conn.recv(65536))
        playerdata[id] = data["player"]
        if playerdata[id].room not in roomstate:
            seed[playerdata[id].room] = random.randint(0, 100000)
            roomstate[playerdata[id].room] = False
            table[playerdata[id].room] = Table()
        if playerdata[id].room not in playerinroom:
            playerinroom[playerdata[id].room] = [playerdata[id]]
        else:
            found = False
            for index in range(len(playerinroom[playerdata[id].room])):
                if playerinroom[playerdata[id].room][index].id == playerdata[id].id:
                    found = True
                    playerinroom[playerdata[id].room][index] = playerdata[id]
                    break
            if not found:
                playerinroom[playerdata[id].room].append(playerdata[id])

        # Checking if the key "gamestart" is in the data dictionary.
        roomstate[playerdata[id].room] = max(
            roomstate[playerdata[id].room], data["gamestart"])

        if "table" in data:
            if data["table"].cardcount >= table[playerdata[id].room].cardcount:
                table[playerdata[id].room] = data["table"]
            if playerdata[id].room not in turn:
                turn[playerdata[id].room] = -1
            if turn[playerdata[id].room] == -1:
                for index in range(len(playerinroom[playerdata[id].room])):
                    if len(playerinroom[playerdata[id].room][index].card) > 0:
                        if playerinroom[playerdata[id].room][index].card[0].name == "club-3.png":
                            turn[playerdata[id].room] = playerdata[id]
                            break
            else:
                if turn[playerdata[id].room].id == playerdata[id].id and playerdata[id].iscompleteturn:
                    print(playerdata[id].name, playerdata[id].iscompleteturn)
                    for index in range(len(playerinroom[playerdata[id].room])):
                        if playerinroom[playerdata[id].room][index].name == turn[playerdata[id].room].name:
                            turn[playerdata[id].room] = playerinroom[playerdata[id].room][(
                                index+1) % 4]
                            playerdata[id].iscompleteturn = False
                            break
        if not data:
            print("Disconnected")
            break
        else:
            if "table" in data:
                reply = {
                    "allplayer": playerdata,
                    "gamestart": roomstate[playerdata[id].room],
                    "seed": seed[playerdata[id].room],
                    "table": table[playerdata[id].room],
                    "turn": turn[playerdata[id].room],
                }
            else:
                reply = {
                    "allplayer": playerdata,
                    "gamestart": roomstate[playerdata[id].room],
                    "seed": seed[playerdata[id].room],
                }
        conn.sendall(pickle.dumps(reply))
        # except Exception as e:
        #     print(e)
        #     break
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
