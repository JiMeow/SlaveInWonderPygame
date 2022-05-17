from threading import *
import py
import pygame
import random
import time

from button import PassButton, PlayButton, PlaceButton
from network import Network
from layout import Layout
from card import Card
from table import Table

from helper import *

# 1536 * 864 -> 768 * 432

# next clear table when every one pass
# update time count down


class Main():
    cardname = [
        'club-1.png', 'club-2.png', 'club-3.png', 'club-4.png', 'club-5.png', 'club-6.png', 'club-7.png', 'club-8.png', 'club-9.png', 'club-T.png',  'club-J.png', 'club-Q.png', 'club-K.png',
        'diamond-1.png', 'diamond-2.png', 'diamond-3.png', 'diamond-4.png', 'diamond-5.png', 'diamond-6.png', 'diamond-7.png', 'diamond-8.png', 'diamond-9.png', 'diamond-T.png', 'diamond-J.png', 'diamond-Q.png', 'diamond-K.png',
        'heart-1.png', 'heart-2.png', 'heart-3.png', 'heart-4.png', 'heart-5.png', 'heart-6.png', 'heart-7.png', 'heart-8.png', 'heart-9.png', 'heart-T.png', 'heart-J.png', 'heart-Q.png', 'heart-K.png',
        'spade-1.png', 'spade-2.png', 'spade-3.png', 'spade-4.png', 'spade-5.png', 'spade-6.png', 'spade-7.png', 'spade-8.png', 'spade-9.png', 'spade-T.png', 'spade-J.png', 'spade-Q.png', 'spade-K.png'
    ]

    card = []
    for name in cardname:
        card.append(Card(name))

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
            "gamestart": 0,
            "table": Table()
        }

        # init layout
        self.layout = Layout(self.win)

        # init thread
        self.thread = Thread(target=getDataFromServer, args=(
            self.network, self.player, self.tempdata))

    def lobby(self):
        # gui in lobby
        run = True
        playbutton = PlayButton(self.win, (718, 382, 100, 100))
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
            self.layout.updateplayButton(playbutton)
            self.layout.updateGamestatus(self.gamestart)
            self.layout.drawlobby()
            # update game status
            self.gamestart = max(self.gamestart, self.layout.gamestart)
            if self.gamestart == 1:
                print("Game start")
                self.game()
            pygame.display.update()

        pygame.quit()
        self.network.disconnect()

    def game(self):
        self.tempdata = {
            "allplayer": dict(self.allplayer),
            "table": Table(),
            "turn": -1,
        }
        # set seed
        random.seed(self.seed)

        # set player in our room
        playerinroom = []
        for id in self.allplayer:
            if self.allplayer[id].room == self.player.room:
                playerinroom.append(self.allplayer[id])
        playerinroom.sort(key=lambda x: x.id)

        # set card and shuffle to others
        card = [Main.card[i-1] for i in range(1, 53)]
        random.shuffle(card)
        for index in range(len(playerinroom)):
            playerinroom[index].card = sorted(card[index*13:index*13+13])
            if playerinroom[index].id == self.player.id:
                self.player = playerinroom[index]

        # game loop
        run = True
        # placebutton = PlaceButton(self.win, (732, 819, 72, 15))
        placebutton = PlaceButton(self.win, (632, 819, 72, 15))
        passbutton = PassButton(self.win, (804, 819, 72, 15))
        table = Table()

        self.thread = Thread(target=getDataFromServerGame, args=(
            self.network, self.player, self.gamestart, table, self.tempdata))

        resettable = False
        while run:
            # set bg as black
            self.win.fill((0, 0, 0))
            # set FPS to 60
            self.clock.tick(60)
            if not self.thread.is_alive():
                # set data from server
                setDataFromServerGame(self.tempdata, self.allplayer, table)
                turn = self.tempdata["turn"]
                # start thread
                if resettable:
                    table.val = 0
                    table.value = 0
                    table.cardtype = ""
                    table.lassplayerid = 0
                    table.cardcount += 1
                    table.keepcard = []
                    table.movecordinate = []
                    table.whopass = []
                self.thread = Thread(target=getDataFromServerGame, args=(
                    self.network, self.player, self.gamestart, table, self.tempdata))
                self.thread.start()
                # reset turn complete
                self.player.iscompleteturn = False
                resettable = False

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
                # handle click on card
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        # get mouse position if click on card
                        if event.pos[0] >= 492 and event.pos[0] <= 492+40*len(self.player.card) and event.pos[1] >= 744 and event.pos[1] <= 804:
                            # get new card index
                            newactive, val = int((event.pos[0]-492)//40), 0
                            nowactive = []
                            # get now active card index and it values
                            for card in self.player.card:
                                if card.active == 1:
                                    nowactive.append(card)
                                    val = card.val
                            # check if click on not same value of activae card cancel active all card else continue
                            if self.player.card[newactive].val != val:
                                for card in nowactive:
                                    card.click()
                                self.player.card[newactive].click()
                            else:
                                self.player.card[newactive].click()
                placebutton.get_event(event)
                passbutton.get_event(event)

            if turn != -1 and self.player.id == turn.id:
                if table.lassplayerid == self.player.id and len(table.whopass) == 3:
                    resettable = True
                # every one pass
                if self.player.id in table.whopass:
                    self.player.iscompleteturn = True
                    table.cardcount += 1

                # check if player press button in his turn
                if placebutton.ispress and self.player.id not in table.whopass:
                    cardcount = table.cardcount
                    table.place(self.player.card, self.player.id)
                    self.player.iscompleteturn = table.cardcount - cardcount
                placebutton.ispress = False

                # check if player press button in his turn
                if passbutton.ispress:
                    if self.player.id not in table.whopass:
                        table.whopass.append(self.player.id)
                    table.cardcount += 1
                    self.player.iscompleteturn = True
                passbutton.ispress = False

            if not self.thread.is_alive():
                # set data from server
                setDataFromServerGame(self.tempdata, self.allplayer, table)
                turn = self.tempdata["turn"]
                if resettable:
                    table.val = 0
                    table.value = 0
                    table.cardtype = ""
                    table.lassplayerid = 0
                    table.cardcount += 100
                    table.keepcard = []
                    table.movecordinate = []
                    table.whopass = []
                # start thread
                self.thread = Thread(target=getDataFromServerGame, args=(
                    self.network, self.player, self.gamestart, table, self.tempdata))
                self.thread.start()
                # reset turn complete
                self.player.iscompleteturn = False
                resettable = False

            # draw all component
            self.layout.updateAllplayer(self.allplayer)
            self.layout.updatePlayer(self.player)
            self.layout.updateplaceButton(placebutton)
            self.layout.updatepassButton(passbutton)
            self.layout.updateGamestatus(self.gamestart)
            self.layout.updateTurn(turn)
            self.layout.updateTable(table)
            self.layout.drawgame()
            pygame.display.update()


game = Main()
game.lobby()
