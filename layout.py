import pygame
from card import Card


def countPlayerinRoom(allplayer, room):
    """
    It counts the number of players in a room

    :param allplayer: a dictionary of all players in the game
    :param room: the room you want to count the players in
    :return: The number of players in a room.
    """
    return sum(player.room == room for id, player in allplayer.items())


class Layout:
    suit_lst = ['club', 'diamond', 'heart', 'spade']
    val_lst = list(map(str, range(1, 10))) + ['T', 'J', 'Q', 'K']
    cardname = []
    for suit in suit_lst:
        for val in val_lst:
            cardname.append(f'{suit}-{val}.png')

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
        allplayer = sorted(self.allplayer.items())
        playertodraw = [player for id,
                        player in allplayer if player.room == myroom]
        while playertodraw[0].id != self.player.id:
            playertodraw.append(playertodraw.pop(0))
        for index, player in enumerate(playertodraw):

            if index == 0:
                if self.playertoplay != -1 and player.id == self.playertoplay.id:
                    pygame.draw.rect(self.win, (238, 0, 0),
                                     (428, 764, 20, 20))
                if player.id in self.table.whopass:
                    textpass = pygame.font.Font(
                        None, 20).render("pass", True, "white")
                    self.win.blit(textpass, textpass.get_rect(
                        center=(428, 794)))

                player.draw(self.win, 468, 764)
                for i in range(len(player.card)):
                    player.card[i].draw(self.win, 498+i*40, 744)

            elif index == 1:
                if self.playertoplay != -1 and player.id == self.playertoplay.id:
                    pygame.draw.rect(self.win, (238, 0, 0),
                                     (60, 412, 20, 20))

                if player.id in self.table.whopass:
                    textpass = pygame.font.Font(
                        None, 20).render("pass", True, "white")
                    self.win.blit(textpass, textpass.get_rect(
                        center=(60, 442)))

                player.draw(self.win, 100, 412)
                textnumberofcard = pygame.font.Font(None, 15).render(
                    f"{len(player.card)}", True, "white"
                )
                self.win.blit(textnumberofcard, textnumberofcard.get_rect(
                    center=(110, 402)))

            elif index == 2:
                if self.playertoplay != -1 and player.id == self.playertoplay.id:
                    pygame.draw.rect(self.win, (238, 0, 0),
                                     (718, 100, 20, 20))

                if player.id in self.table.whopass:
                    textpass = pygame.font.Font(
                        None, 20).render("pass", True, "white")
                    self.win.blit(textpass, textpass.get_rect(
                        center=(718, 130)))

                player.draw(self.win, 758, 100)
                textnumberofcard = pygame.font.Font(None, 15).render(
                    f"{len(player.card)}", True, "white"
                )
                self.win.blit(textnumberofcard, textnumberofcard.get_rect(
                    center=(768, 90)))

            elif index == 3:
                if self.playertoplay != -1 and player.id == self.playertoplay.id:
                    pygame.draw.rect(self.win, (238, 0, 0),
                                     (1386, 412, 20, 20))

                if player.id in self.table.whopass:
                    textpass = pygame.font.Font(
                        None, 20).render("pass", True, "white")
                    self.win.blit(textpass, textpass.get_rect(
                        center=(1386, 442)))

                player.draw(self.win, 1426, 412)
                textnumberofcard = pygame.font.Font(None, 15).render(
                    f"{len(player.card)}", True, "white"
                )
                self.win.blit(textnumberofcard, textnumberofcard.get_rect(
                    center=(1436, 402)))

        textroom = pygame.font.Font(None, 30).render(
            f"room id: {myroom}", True, "white"
        )
        self.win.blit(textroom, (10, 10))

        textstart = pygame.font.Font(None, 30).render(
            "Start game", True, "white")
        self.win.blit(textstart, (10, 50))

        if self.playertoplay != -1:
            textturn = pygame.font.Font(None, 30).render(
                f"Turn: {self.playertoplay.name}", True, "white"
            )
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
        allplayer = sorted(self.allplayer.items())
        playertodraw = [player for id,
                        player in allplayer if player.room == myroom]
        while playertodraw[0].id != self.player.id:
            playertodraw.append(playertodraw.pop(0))
        for index, player in enumerate(playertodraw):
            if index == 0:
                if self.playertoplay != -1 and player.id == self.playertoplay.id:
                    pygame.draw.rect(self.win, (238, 0, 0),
                                     (428, 764, 20, 20))
                if player.id in self.table.whopass:
                    textpass = pygame.font.Font(
                        None, 20).render("pass", True, "white")
                    self.win.blit(textpass, textpass.get_rect(
                        center=(428, 794)))

                player.draw(self.win, 468, 764)
                for i in range(len(player.card)):
                    player.card[i].draw(self.win, 498+i*40, 744)

            elif index == 1:
                if self.playertoplay != -1 and player.id == self.playertoplay.id:
                    pygame.draw.rect(self.win, (238, 0, 0),
                                     (60, 412, 20, 20))

                if player.id in self.table.whopass:
                    textpass = pygame.font.Font(
                        None, 20).render("pass", True, "white")
                    self.win.blit(textpass, textpass.get_rect(
                        center=(60, 442)))

                player.draw(self.win, 100, 412)
                textnumberofcard = pygame.font.Font(None, 15).render(
                    f"{len(player.card)}", True, "white"
                )
                self.win.blit(textnumberofcard, textnumberofcard.get_rect(
                    center=(110, 402)))

            elif index == 2:
                if self.playertoplay != -1 and player.id == self.playertoplay.id:
                    pygame.draw.rect(self.win, (238, 0, 0),
                                     (718, 100, 20, 20))

                if player.id in self.table.whopass:
                    textpass = pygame.font.Font(
                        None, 20).render("pass", True, "white")
                    self.win.blit(textpass, textpass.get_rect(
                        center=(718, 130)))

                player.draw(self.win, 758, 100)
                textnumberofcard = pygame.font.Font(None, 15).render(
                    f"{len(player.card)}", True, "white"
                )
                self.win.blit(textnumberofcard, textnumberofcard.get_rect(
                    center=(768, 90)))

            elif index == 3:
                if self.playertoplay != -1 and player.id == self.playertoplay.id:
                    pygame.draw.rect(self.win, (238, 0, 0),
                                     (1386, 412, 20, 20))

                if player.id in self.table.whopass:
                    textpass = pygame.font.Font(
                        None, 20).render("pass", True, "white")
                    self.win.blit(textpass, textpass.get_rect(
                        center=(1386, 442)))

                player.draw(self.win, 1426, 412)
                textnumberofcard = pygame.font.Font(None, 15).render(
                    f"{len(player.card)}", True, "white"
                )
                self.win.blit(textnumberofcard, textnumberofcard.get_rect(
                    center=(1436, 402)))

        textroom = pygame.font.Font(None, 30).render(
            f"room id: {myroom}", True, "white"
        )
        self.win.blit(textroom, (10, 10))

        textstart = pygame.font.Font(None, 30).render(
            "Start game", True, "white")
        self.win.blit(textstart, (10, 50))

        if self.playertoplay != -1:
            textturn = pygame.font.Font(None, 30).render(
                f"Turn: {self.playertoplay.name}", True, "white"
            )
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
        allplayer = sorted(self.allplayer.items())
        playertodraw = [player for id,
                        player in allplayer if player.room == myroom]
        while playertodraw[0].id != self.player.id:
            playertodraw.append(playertodraw.pop(0))
        for index, player in enumerate(playertodraw):
            if index == 0:
                player.draw(self.win, 758, 744)
            elif index == 1:
                player.draw(self.win, 100, 412)
            elif index == 2:
                player.draw(self.win, 758, 100)
            elif index == 3:
                player.draw(self.win, 1426, 412)
        textroom = pygame.font.Font(None, 30).render(
            f"room id: {myroom}", True, "white"
        )
        self.win.blit(textroom, (10, 10))
        self.playbutton.draw()

        if self.playbutton.ispress > 0 and countPlayerinRoom(self.allplayer, self.player.room) == 4:
            self.gamestart = 1
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
