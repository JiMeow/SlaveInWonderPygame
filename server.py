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
direction = {}
# key: room, value: class player
turn = {}

# key: room, value: List[players] in the room
playerinroom = {}

# key: room, value: List[players] in the room (already win)
winner = {}

seed = {}

winner["1"] = [Player(1, "black"), Player(2, "black"),
               Player(3, "black"), Player(4, "black"), ]


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
        # keep player data from client in server
        playerdata[id] = data["player"]
        # set default value of dict
        room = playerdata[id].room

        if room not in roomstate:
            seed[room] = random.randint(0, 100000)
            roomstate[room] = False
            table[room] = Table()
            direction[room] = 1
        # set default value of playerinroom
        if room not in playerinroom:
            playerinroom[room] = [playerdata[id]]
        else:
            # assign new player value in same player id
            found = False
            for index in range(len(playerinroom[room])):
                if playerinroom[room][index].id == playerdata[id].id:
                    found = True
                    playerinroom[room][index] = playerdata[id]
                    break
            if not found:
                playerinroom[room].append(playerdata[id])

        # update game state
        roomstate[room] = max(
            roomstate[room], data["gamestart"])

        # if game start
        if "table" in data:
            if data["gamestate"] == "phrase1":
                # update table if table from client is newer than server by check cardcount
                if data["table"].cardcount > table[room].cardcount:
                    table[room] = data["table"]

                if len(playerdata[id].card) == 0:
                    if room not in winner:
                        winner[room] = []
                    if playerdata[id] not in winner[room]:
                        if len(data["table"].whopass) == 3:
                            direction[room] *= -1
                        winner[room].append(playerdata[id])
                    # for player in winner[room]:
                    #     print(player.name, end=' ')
                    # print()

                # set default value of turn
                if room not in turn:
                    turn[room] = -1
                # find club-3 card to set first player
                if turn[room] == -1:
                    for index in range(len(playerinroom[room])):
                        if len(playerinroom[room][index].card) > 0:
                            if playerinroom[room][index].card[0].name == "club-3.png":
                                turn[room] = playerdata[id]
                                break
                else:
                    # set another player to turn
                    if turn[room].id == playerdata[id].id and playerdata[id].iscompleteturn:
                        print(playerdata[id].name,
                              playerdata[id].iscompleteturn)
                        for index in range(len(playerinroom[room])):
                            if playerinroom[room][index].name == turn[room].name:
                                turn[room] = playerinroom[room][(
                                    index+direction[room]) % 4]
                                playerdata[id].iscompleteturn = False
                                break

            if data["gamestate"] == "phrase2":
                # update table if table from client is newer than server by check cardcount
                if data["table"].cardcount > table[room].cardcount:
                    table[room] = data["table"]
                    winner[room] = data["winner"]
                if len(playerdata[id].card) == 0:
                    if room not in winner:
                        winner[room] = []
                    if playerdata[id] not in winner[room]:
                        if len(data["table"].whopass) == 3:
                            direction[room] *= -1
                        winner[room].append(playerdata[id])
                    # for player in winner[room]:
                    #     print(player.name, end=' ')
                    # print()

                # set default value of turn
                if room not in turn:
                    turn[room] = -1
                # find club-3 card to set first player
                if turn[room] == -1:
                    turn[room] = winner["1"][-1]
                else:
                    # set another player to turn
                    if playerdata[id].iscompleteturn == True:
                        print(turn[room].id, playerdata[id].id,
                            playerdata[id].iscompleteturn)
                    if turn[room].id == playerdata[id].id and playerdata[id].iscompleteturn:
                        for index in range(len(playerinroom[room])):
                            if playerinroom[room][index].name == turn[room].name:
                                turn[room] = playerinroom[room][(
                                    index+direction[room]) % 4]
                                playerdata[id].iscompleteturn = False
                                break

        if not data:
            print("Disconnected")
            break
        else:
            # if game start
            if "table" in data:
                if data["gamestate"] == "phrase1":
                    reply = {
                        "allplayer": playerdata,
                        "gamestart": roomstate[room],
                        "seed": seed[room],
                        "table": table[room],
                        "turn": turn[room],
                    }
                if data["gamestate"] == "phrase2":
                    reply = {
                        "allplayer": playerdata,
                        "gamestart": roomstate[room],
                        "seed": seed[room],
                        "table": table[room],
                        "turn": turn[room],
                        "winner": winner[room],
                    }
            # if in lobby
            else:
                reply = {
                    "allplayer": playerdata,
                    "gamestart": roomstate[room],
                    "seed": seed[room],
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
