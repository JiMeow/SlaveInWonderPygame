import pygame
from player import Player
from card import Card


def countPlayerinRoom(allplayer, room):
    ans = 0
    for id, player in allplayer.items():
        if player.room == room:
            ans += 1
    return ans


class Layout:
    cardname = [
        'club-1.png', 'club-2.png', 'club-3.png', 'club-4.png', 'club-5.png', 'club-6.png', 'club-7.png', 'club-8.png', 'club-9.png', 'club-T.png',  'club-J.png', 'club-Q.png', 'club-K.png',
        'diamond-1.png', 'diamond-2.png', 'diamond-3.png', 'diamond-4.png', 'diamond-5.png', 'diamond-6.png', 'diamond-7.png', 'diamond-8.png', 'diamond-9.png', 'diamond-T.png', 'diamond-J.png', 'diamond-Q.png', 'diamond-K.png',
        'heart-1.png', 'heart-2.png', 'heart-3.png', 'heart-4.png', 'heart-5.png', 'heart-6.png', 'heart-7.png', 'heart-8.png', 'heart-9.png', 'heart-T.png', 'heart-J.png', 'heart-Q.png', 'heart-K.png',
        'spade-1.png', 'spade-2.png', 'spade-3.png', 'spade-4.png', 'spade-5.png', 'spade-6.png', 'spade-7.png', 'spade-8.png', 'spade-9.png', 'spade-T.png', 'spade-J.png', 'spade-Q.png', 'spade-K.png'
    ]

    card = []
    for name in cardname:
        card.append(Card(name))

    def __init__(self, win):
        self.win = win
        self.gamestart = 0

    def updateAllplayer(self, allplayer):
        self.allplayer = allplayer

    def updatePlayer(self, player):
        self.player = player

    def updateButton(self, button):
        self.button = button

    def updateGamestatus(self, gamestart):
        self.gamestart = gamestart

    def drawgame(self):
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
                player.draw(self.win, 468, 764)
                for i in range(len(player.card)):
                    player.card[i].draw(self.win, 498+i*40, 744)
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

        textstart = pygame.font.Font(None, int(30)).render(
            "Start game", True, "white")
        self.win.blit(textstart, (10, 50))

        self.button.draw()
        pygame.display.update()

    def drawlobby(self):
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
            self.button.ispress = 0
            self.gamestart = 1
        else:
            self.button.ispress = 0

        pygame.display.update()
