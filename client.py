from threading import *
import py
import pygame
import time

from network import Network
from layout import Layout


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
        self.layout = Layout(self.win)

    def play(self):
        self.run = True
        self.win.fill((0, 0, 0))
        while self.run:
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
            self.clock.tick(60)
            self.allplayer = self.network.send(self.player)["allplayer"]
            self.layout.updateAllplayer(self.allplayer)
            self.layout.updatePlayer(self.player)
            self.layout.draw()
            pygame.display.update()
        pygame.quit()
        # self.network.disconnect()


game = Main()
game.play()
