from threading import *
import py
import pygame
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

        # gui in lobby
        self.playbutton = Button(self.win, (718, 382, 100, 100))

    def play(self):
        self.run = True
        while self.run:
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
                # check if click play button
                self.playbutton.get_event(event)

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
            self.layout.updateButton(self.playbutton)
            self.layout.draw()
            # update game status
            self.gamestart = max(self.gamestart, self.layout.gamestart)
            print(self.gamestart)
            pygame.display.update()

        pygame.quit()
        self.network.disconnect()


game = Main()
game.play()
