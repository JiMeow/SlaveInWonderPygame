import pygame
from player import Player


def countPlayerinRoom(allplayer, room):
    ans = 0
    for id, player in allplayer.items():
        if player.room == room:
            ans += 1
    return ans


class Layout:
    def __init__(self, win):
        self.win = win
        self.gamestart = 0

    def updateAllplayer(self, allplayer):
        self.allplayer = allplayer

    def updatePlayer(self, player):
        self.player = player

    def updateButton(self, button):
        self.button = button

    def draw(self):
        myroom = self.player.room
        allplayer = list(self.allplayer.items())
        allplayer.sort()
        playertodraw = []
        for id, player in allplayer:
            if player.room == myroom:
                playertodraw.append(player)
        while playertodraw[0].id != self.player.id:
            playertodraw.append(playertodraw.pop(0))
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

        textroom = pygame.font.Font(None, int(30)).render(
            f"room id: {myroom}", True, "white")
        self.win.blit(textroom, (10, 10))
        self.button.draw()

        if self.button.ispress > 0 and countPlayerinRoom(self.allplayer, self.player.room) == 4:
            print("start")
            textstart = pygame.font.Font(None, int(30)).render(
                "Start game", True, "white")
            self.win.blit(textstart, (10, 50))
            self.button.ispress = 0
            self.gamestart = 1
        else:
            self.button.ispress = 0

        pygame.display.update()
