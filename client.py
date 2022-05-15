from threading import *
import py
import pygame
import random
import time

from button import Button
from network import Network
from layout import Layout

from helper import *

# 1536 * 864 -> 768 * 432


class Main():

    def __init__(self):

        # accept player name and room id from user
        name = input("Enter your name: ")
        room = input("Enter room id: ")
        # init network
        self.network = Network()
        # init pygame
        self.win = pygame.display.set_mode((1536, 864))
        pygame.display.set_caption("SlaveWonderPygame")
        pygame.init()
        self.clock = pygame.time.Clock()

        # init ourself (player)
        self.player = self.network.getInitData()
        self.player.name = name
        self.player.room = room

        # init all player and gamestatus
        tempdata = self.network.send({
            "player": self.player,
            "gamestart": 0
        })
        self.allplayer = tempdata["allplayer"]
        self.gamestart = tempdata["gamestart"]
        self.seed = tempdata["seed"]

        # init data for accept data from server
        self.tempdata = {
            "allplayer": dict(self.allplayer),
            "gamestart": 0
        }

        # init layout
        self.layout = Layout(self.win)

        # init thread
        self.thread = Thread(target=getDataFromServer, args=(
            self.network, self.player, self.tempdata))

    def lobby(self):
        # gui in lobby
        run = True
        playbutton = Button(self.win, (718, 382, 100, 100))
        while run:
            # set bg as black
            self.win.fill((0, 0, 0))
            # set FPS to 60
            self.clock.tick(60)
            if not self.thread.is_alive():
                # set data from server
                setDataFromServer(self.tempdata, self.allplayer)
                self.gamestart = max(
                    self.gamestart, self.tempdata["gamestart"])
                # start thread
                self.thread = Thread(target=getDataFromServer, args=(
                    self.network, self.player, self.gamestart, self.tempdata))
                self.thread.start()

            # handle all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    self.network.disconnect()
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.run = False
                        pygame.quit()
                        self.network.disconnect()
                        break
                if self.gamestart == 0:
                    # check if click play button
                    playbutton.get_event(event)

            if not self.thread.is_alive():
                # set data from server
                setDataFromServer(self.tempdata, self.allplayer)
                self.gamestart = max(
                    self.gamestart, self.tempdata["gamestart"])
                # start thread
                self.thread = Thread(target=getDataFromServer, args=(
                    self.network, self.player, self.gamestart, self.tempdata))
                self.thread.start()

            # draw all component
            self.layout.updateAllplayer(self.allplayer)
            self.layout.updatePlayer(self.player)
            self.layout.updateButton(playbutton)
            self.layout.updateGamestatus(self.gamestart)
            self.layout.drawlobby()
            # update game status
            self.gamestart = max(self.gamestart, self.layout.gamestart)
            if self.gamestart == 1:
                self.game()
            pygame.display.update()

        pygame.quit()
        self.network.disconnect()

    def game(self):
        random.seed(self.seed)
        playerinroom = []
        for id in self.allplayer:
            if self.allplayer[id].room == self.player.room:
                playerinroom.append(self.allplayer[id])
        playerinroom.sort(key=lambda x: x.id)
        card = [i for i in range(1, 53)]
        random.shuffle(card)
        for index in range(len(playerinroom)):
            # playerinroom[index].card = sorted(
            #     card[index*13:index*13+13], key=lambda x: ((x-1) % 13, (x-1)//13))
            playerinroom[index].card = card[index*13:index*13+13]
            if playerinroom[index].id == self.player.id:
                self.player = playerinroom[index]

        run = True
        while run:
            # set bg as black
            self.win.fill((0, 0, 0))
            # set FPS to 60
            self.clock.tick(60)
            if not self.thread.is_alive():
                # set data from server
                setDataFromServer(self.tempdata, self.allplayer)
                # start thread
                self.thread = Thread(target=getDataFromServer, args=(
                    self.network, self.player, self.gamestart, self.tempdata))
                self.thread.start()

            # handle all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    self.network.disconnect()
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.run = False
                        pygame.quit()
                        self.network.disconnect()
                        break

            if not self.thread.is_alive():
                # set data from server
                setDataFromServer(self.tempdata, self.allplayer)
                # start thread
                self.thread = Thread(target=getDataFromServer, args=(
                    self.network, self.player, self.gamestart, self.tempdata))
                self.thread.start()

            # draw all component
            self.layout.updateAllplayer(self.allplayer)
            self.layout.updatePlayer(self.player)
            self.layout.updateGamestatus(self.gamestart)
            self.layout.drawgame()
            # update game status
            self.gamestart = max(self.gamestart, self.layout.gamestart)
            pygame.display.update()


game = Main()
game.lobby()
