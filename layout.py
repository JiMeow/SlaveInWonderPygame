import pygame
from player import Player
from card import Card


def countPlayerinRoom(allplayer, room):
    """
    It counts the number of players in a room

    :param allplayer: a dictionary of all players in the game
    :param room: the room you want to count the players in
    :return: The number of players in a room.
    """
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
        """
        The function __init__ is a constructor that initializes the class

        :param win: The window that the game is being played in
        """
        self.win = win
        self.gamestart = 0

    def drawgamephase1(self):
        """
        It draws the game
        """
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
                if self.playertoplay != -1 and player.id == self.playertoplay.id:
                    pygame.draw.rect(self.win, (238, 0, 0),
                                     (428, 764, 20, 20))
                if player.id in self.table.whopass:
                    textpass = pygame.font.Font(None, int(20)).render(
                        f"pass", True, "white")
                    self.win.blit(textpass, textpass.get_rect(
                        center=(428, 794)))

                player.draw(self.win, 468, 764)
                for i in range(len(player.card)):
                    player.card[i].draw(self.win, 498+i*40, 744)

            if index == 1:
                if self.playertoplay != -1 and player.id == self.playertoplay.id:
                    pygame.draw.rect(self.win, (238, 0, 0),
                                     (60, 412, 20, 20))

                if player.id in self.table.whopass:
                    textpass = pygame.font.Font(None, int(20)).render(
                        f"pass", True, "white")
                    self.win.blit(textpass, textpass.get_rect(
                        center=(60, 442)))

                player.draw(self.win, 100, 412)
                textnumberofcard = pygame.font.Font(None, int(15)).render(
                    f"{len(player.card)}", True, "white")
                self.win.blit(textnumberofcard, textnumberofcard.get_rect(
                    center=(110, 402)))

            if index == 2:
                if self.playertoplay != -1 and player.id == self.playertoplay.id:
                    pygame.draw.rect(self.win, (238, 0, 0),
                                     (718, 100, 20, 20))

                if player.id in self.table.whopass:
                    textpass = pygame.font.Font(None, int(20)).render(
                        f"pass", True, "white")
                    self.win.blit(textpass, textpass.get_rect(
                        center=(718, 130)))

                player.draw(self.win, 758, 100)
                textnumberofcard = pygame.font.Font(None, int(15)).render(
                    f"{len(player.card)}", True, "white")
                self.win.blit(textnumberofcard, textnumberofcard.get_rect(
                    center=(768, 90)))

            if index == 3:
                if self.playertoplay != -1 and player.id == self.playertoplay.id:
                    pygame.draw.rect(self.win, (238, 0, 0),
                                     (1386, 412, 20, 20))

                if player.id in self.table.whopass:
                    textpass = pygame.font.Font(None, int(20)).render(
                        f"pass", True, "white")
                    self.win.blit(textpass, textpass.get_rect(
                        center=(1386, 442)))

                player.draw(self.win, 1426, 412)
                textnumberofcard = pygame.font.Font(None, int(15)).render(
                    f"{len(player.card)}", True, "white")
                self.win.blit(textnumberofcard, textnumberofcard.get_rect(
                    center=(1436, 402)))

            index += 1

        textroom = pygame.font.Font(None, int(30)).render(
            f"room id: {myroom}", True, "white")
        self.win.blit(textroom, (10, 10))

        textstart = pygame.font.Font(None, int(30)).render(
            "Start game", True, "white")
        self.win.blit(textstart, (10, 50))

        if self.playertoplay != -1:
            textturn = pygame.font.Font(None, int(30)).render(
                f"Turn: {self.playertoplay.name}", True, "white")
            self.win.blit(textturn, (10, 90))

        self.placebutton.draw()
        self.passbutton.draw()
        self.table.draw(self.win)
        pygame.display.update()

    def drawgamephase2(self):
        """
        It draws the game
        """
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
                if self.playertoplay != -1 and player.id == self.playertoplay.id:
                    pygame.draw.rect(self.win, (238, 0, 0),
                                     (428, 764, 20, 20))
                if player.id in self.table.whopass:
                    textpass = pygame.font.Font(None, int(20)).render(
                        f"pass", True, "white")
                    self.win.blit(textpass, textpass.get_rect(
                        center=(428, 794)))

                player.draw(self.win, 468, 764)
                for i in range(len(player.card)):
                    player.card[i].draw(self.win, 498+i*40, 744)

            if index == 1:
                if self.playertoplay != -1 and player.id == self.playertoplay.id:
                    pygame.draw.rect(self.win, (238, 0, 0),
                                     (60, 412, 20, 20))

                if player.id in self.table.whopass:
                    textpass = pygame.font.Font(None, int(20)).render(
                        f"pass", True, "white")
                    self.win.blit(textpass, textpass.get_rect(
                        center=(60, 442)))

                player.draw(self.win, 100, 412)
                textnumberofcard = pygame.font.Font(None, int(15)).render(
                    f"{len(player.card)}", True, "white")
                self.win.blit(textnumberofcard, textnumberofcard.get_rect(
                    center=(110, 402)))

            if index == 2:
                if self.playertoplay != -1 and player.id == self.playertoplay.id:
                    pygame.draw.rect(self.win, (238, 0, 0),
                                     (718, 100, 20, 20))

                if player.id in self.table.whopass:
                    textpass = pygame.font.Font(None, int(20)).render(
                        f"pass", True, "white")
                    self.win.blit(textpass, textpass.get_rect(
                        center=(718, 130)))

                player.draw(self.win, 758, 100)
                textnumberofcard = pygame.font.Font(None, int(15)).render(
                    f"{len(player.card)}", True, "white")
                self.win.blit(textnumberofcard, textnumberofcard.get_rect(
                    center=(768, 90)))

            if index == 3:
                if self.playertoplay != -1 and player.id == self.playertoplay.id:
                    pygame.draw.rect(self.win, (238, 0, 0),
                                     (1386, 412, 20, 20))

                if player.id in self.table.whopass:
                    textpass = pygame.font.Font(None, int(20)).render(
                        f"pass", True, "white")
                    self.win.blit(textpass, textpass.get_rect(
                        center=(1386, 442)))

                player.draw(self.win, 1426, 412)
                textnumberofcard = pygame.font.Font(None, int(15)).render(
                    f"{len(player.card)}", True, "white")
                self.win.blit(textnumberofcard, textnumberofcard.get_rect(
                    center=(1436, 402)))

            index += 1

        textroom = pygame.font.Font(None, int(30)).render(
            f"room id: {myroom}", True, "white")
        self.win.blit(textroom, (10, 10))

        textstart = pygame.font.Font(None, int(30)).render(
            "Start game", True, "white")
        self.win.blit(textstart, (10, 50))

        if self.playertoplay != -1:
            textturn = pygame.font.Font(None, int(30)).render(
                f"Turn: {self.playertoplay.name}", True, "white")
            self.win.blit(textturn, (10, 90))

        self.placebutton.draw()
        self.passbutton.draw()
        self.switchbutton.draw()
        self.table.draw(self.win)
        pygame.display.update()

    def drawlobby(self):
        """
        It draws the lobby
        """
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
        self.playbutton.draw()

        if self.playbutton.ispress > 0 and countPlayerinRoom(self.allplayer, self.player.room) == 4:
            self.playbutton.ispress = 0
            self.gamestart = 1
        else:
            self.playbutton.ispress = 0

        pygame.display.update()

    def updateAllplayer(self, allplayer):
        """
        It takes a list of all players and updates the list of all players

        :param allplayer: a list of all the players in the game
        """
        self.allplayer = allplayer

    def updatePlayer(self, player):
        """
        The function takes in a player object and updates the player object in the game class to the
        player object passed in

        :param player: The player object
        """
        self.player = player

    def updateplayButton(self, button):
        """
        The function takes in a button as an argument and sets the playbutton variable to the button

        :param button: The button that is being updated
        """
        self.playbutton = button

    def updateplaceButton(self, placeButton):
        """
        The function takes in a placeButton and sets the placeButton to the placeButton that was passed
        in

        :param placeButton: The button that is being updated
        """
        self.placebutton = placeButton

    def updatepassButton(self, passButton):
        """
        The function takes in a button and sets it as the pass button

        :param passButton: The button that is clicked to pass the turn
        """
        self.passbutton = passButton

    def updateGamestatus(self, gamestart):
        """
        The function takes in a boolean value and sets the value of the gamestart variable to the value
        of the boolean value

        :param gamestart: Boolean
        """
        self.gamestart = gamestart

    def updateTable(self, table):
        """
        It takes a table as an argument and sets the table attribute of the object to the table argument

        :param table: the table to update
        """
        self.table = table

    def updateTurn(self, playertoplay):
        """
        It takes the current player to play and updates the player to play to the next player

        :param playertoplay: The player who's turn it is to play
        """
        self.playertoplay = playertoplay

    def updateswitchButton(self, switchButton):
        """
        It takes in a switchButton and sets it as the switchButton

        :param switchButton: The button that is clicked to switch the card
        """
        self.switchbutton = switchButton
