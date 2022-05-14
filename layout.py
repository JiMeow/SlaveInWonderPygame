import pygame
from player import Player


class Layout:
    def __init__(self, win):
        self.win = win

    def updateAllplayer(self, allplayer):
        self.allplayer = allplayer

    def updatePlayer(self, player):
        self.player = player

    def draw(self):
        myroom = self.player.room
        allplayer = list(self.allplayer.items())
        allplayer.sort()
        print(allplayer)
        playertodraw = []
        for id, player in allplayer:
            if player.room == myroom:
                playertodraw.append(player)
        while playertodraw[0].id != self.player.id:
            playertodraw.append(playertodraw.pop(0))
        print("playertodraw", playertodraw)
        index = 0
        for player in playertodraw:
            if index == 0:
                player.draw(self.win, 758, 744)
            if index == 1:
                player.draw(self.win, 100, 412)
            if index == 2:
                player.draw(self.win, 758, 100)
            if index == 3:
                player.draw(self.win, 1426, 412)
            index += 1
        pygame.display.update()
