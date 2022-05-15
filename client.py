from threading import *
import py
import pygame
import time

from button import Button
from network import Network
from layout import Layout

from helper import *


class Main():
    def __init__(self):
        name = input("Enter your name: ")
        room = input("Enter room id: ")
        self.network = Network()
        self.win = pygame.display.set_mode((1536, 864))
        pygame.display.set_caption("SlaveWonderPygame")
        pygame.init()
        self.clock = pygame.time.Clock()
        self.player = self.network.getInitData()
        self.player.name = name
        self.player.room = room
        self.allplayer = self.network.send(self.player)["allplayer"]

        self.tempdata = {
            "allplayer": dict(self.allplayer)
        }
        self.layout = Layout(self.win)

        self.thread = Thread(target=getDataFromServer, args=(
            self.network, self.player, self.tempdata))

    def play(self):
        self.run = True
        self.win.fill((0, 0, 0))
        while self.run:
            self.clock.tick(60)

            if not self.thread.is_alive():
                setDataFromServer(self.tempdata, self.allplayer)
                self.thread = Thread(target=getDataFromServer, args=(
                    self.network, self.player, self.tempdata))
                self.thread.start()

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
                setDataFromServer(self.tempdata, self.allplayer)
                self.thread = Thread(target=getDataFromServer, args=(
                    self.network, self.player, self.tempdata))
                self.thread.start()

            playbutton = Button(self.win, (10, 10, 100, 100))

            self.layout.updateAllplayer(self.allplayer)
            self.layout.updatePlayer(self.player)
            self.layout.draw()
            pygame.display.update()

        pygame.quit()
        self.network.disconnect()


game = Main()
game.play()
