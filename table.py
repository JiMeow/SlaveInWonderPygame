import pygame
import random
import time

from card import Card


class Table:
    suit_lst = ['club', 'diamond', 'heart', 'spade']
    val_lst = list(map(str, range(1, 10))) + ['T', 'J', 'Q', 'K']
    cardname = []
    for suit in suit_lst:
        for val in val_lst:
            cardname.append(f'{suit}-{val}.png')

    card = []
    for name in cardname:
        card.append(Card(name))

    def __init__(self):
        """
        The function is called when the player clicks on the card
        """
        self.val = 0
        self.value = 0
        self.cardtype = ""
        self.cardcount = 0
        self.keepcard = []
        self.movecordinate = []
        self.rect = pygame.Rect((718, 382, 100, 100))
        self.lassplayerid = 0
        self.whopass = []

    def draw(self, screen):
        """
        It draws the last 5 cards that were played on the screen

        :param screen: The screen that the cards will be draw on
        """
        self.keepcard = self.keepcard[-5:]
        self.movecordinate = self.movecordinate[-5:]
        for historyindex, listcard in enumerate(self.keepcard):
            rect = pygame.Rect((0, 0, 0, 0))
            rect.center = (
                self.rect.center[0], self.rect.center[1])
            for index in range(len(listcard)):
                name, angle = listcard[index]
                img = pygame.transform.rotate(pygame.transform.scale(
                    pygame.image.load(f"{name}"), (40, 60)), angle)
                if len(listcard) == 1:
                    screen.blit(
                        img, (rect.x+self.movecordinate[historyindex][index][0], rect.y+self.movecordinate[historyindex][index][1], 40, 60))
                if len(listcard) == 2:
                    screen.blit(
                        img, (rect.x-15+index*30+self.movecordinate[historyindex][index][0], rect.y+self.movecordinate[historyindex][index][1], 40, 60))
                if len(listcard) == 3:
                    screen.blit(
                        img, (rect.x-30+index*30+self.movecordinate[historyindex][index][0], rect.y+self.movecordinate[historyindex][index][1], 40, 60))
                if len(listcard) == 4:
                    screen.blit(
                        img, (rect.x-45+index*30+self.movecordinate[historyindex][index][0], rect.y+self.movecordinate[historyindex][index][1], 40, 60))

    def place(self, listcard, playerid):
        """
        If the card is a zero, place the card. If the card is odd, place the card if the value of the
        card is greater than the value of the card on the board. If the card is even, place the card if
        the value of the card is greater than the value of the card on the board

        :param listcard: list of cards
        """
        activecard = [card for card in listcard if card.active]
        if self.value == 0:
            self.setcardhere(activecard, playerid)
            for card in activecard:
                listcard.remove(card)
        elif self.cardtype == "odd":
            if len(activecard) == 1:
                if activecard[-1].value > self.value:
                    self.setcardhere(activecard, playerid)
                    for card in activecard:
                        listcard.remove(card)
            elif len(activecard) == 3:
                if activecard[-1].value*1000 > self.value:
                    self.setcardhere(activecard, playerid)
                    for card in activecard:
                        listcard.remove(card)
        elif self.cardtype == "even":
            if len(activecard) == 2:
                if activecard[-1].value > self.value:
                    self.setcardhere(activecard, playerid)
                    for card in activecard:
                        listcard.remove(card)
            elif len(activecard) == 4:
                if activecard[-1].value*1000 > self.value:
                    self.setcardhere(activecard, playerid)
                    for card in activecard:
                        listcard.remove(card)

    def setcardhere(self, activecard, playerid):
        """
        It takes a list of cards, and then randomly rotates each card and places it on the screen

        :param activecard: list of cards
        """
        random.seed(int(time.time()))
        if len(activecard) == 1:
            self.val = activecard[0].val
            self.value = activecard[-1].value
            angletorotate = random.randint(-30, 30)
            data = [(f"photo/cardsprite/{activecard[0].name}", angletorotate)]
            self.keepcard.append(data)
            self.movecordinate.append(
                [(random.randint(-10, 10), random.randint(-10, 10))])
        if len(activecard) == 2:
            self.val = activecard[0].val
            self.value = activecard[-1].value
            angletorotate = random.randint(-30, 30)
            img = [pygame.transform.rotate(pygame.transform.scale(
                pygame.image.load(f"photo/cardsprite/{activecard[i].name}"), (40, 60)), angletorotate) for i in range(2)]
            data = [
                (f"photo/cardsprite/{activecard[i].name}", angletorotate) for i in range(2)]
            self.keepcard.append(data)
            self.movecordinate.append(
                [
                    (random.randint(-10, 10), random.randint(-10, 10))
                    for _ in range(2)
                ]
            )
        if len(activecard) == 3:
            self.val = activecard[0].val
            self.value = activecard[-1].value*1000
            angletorotate = random.randint(-30, 30)
            img = [pygame.transform.rotate(pygame.transform.scale(
                pygame.image.load(f"photo/cardsprite/{activecard[i].name}"), (40, 60)), angletorotate) for i in range(3)]
            data = [
                (f"photo/cardsprite/{activecard[i].name}", angletorotate) for i in range(3)]
            self.keepcard.append(data)
            self.movecordinate.append(
                [
                    (random.randint(-10, 10), random.randint(-10, 10))
                    for _ in range(3)
                ]
            )
        if len(activecard) == 4:
            self.val = activecard[0].val
            self.value = activecard[-1].value*1000
            angletorotate = random.randint(-30, 30)
            img = [pygame.transform.rotate(pygame.transform.scale(
                pygame.image.load(f"photo/cardsprite/{activecard[i].name}"), (40, 60)), angletorotate) for i in range(3)]
            data = [
                (f"photo/cardsprite/{activecard[i].name}", angletorotate) for i in range(3)]
            self.keepcard.append(data)
            self.movecordinate.append(
                [
                    (random.randint(-10, 10), random.randint(-10, 10))
                    for _ in range(4)
                ]
            )
        self.cardtype = "odd" if len(activecard) % 2 == 1 else "even"
        self.lassplayerid = playerid
        self.cardcount += 1
