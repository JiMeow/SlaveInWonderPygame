import pygame
import random

from card import Card


class Table:

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
        self.val = 0
        self.value = 0
        self.cardtype = ""
        self.keepcard = []
        self.movecordinate = []
        self.rect = pygame.Rect((718, 382, 100, 100))

    def draw(self, screen):
        historyindex = 0
        for listcard in self.keepcard:
            rect = pygame.Rect((0, 0, 0, 0))
            rect.center = (
                self.rect.center[0], self.rect.center[1])
            for index in range(len(listcard)):
                if len(listcard) == 1:
                    screen.blit(
                        listcard[index], (rect.x+self.movecordinate[historyindex][0], rect.y+self.movecordinate[historyindex][1], 40, 60))
                if len(listcard) == 2:
                    screen.blit(
                        listcard[index], (rect.x-20+index*40+self.movecordinate[historyindex][0], rect.y+self.movecordinate[historyindex][1], 40, 60))
                if len(listcard) == 3:
                    screen.blit(
                        listcard[index], (rect.x-40+index*40+self.movecordinate[historyindex][0], rect.y+self.movecordinate[historyindex][1], 40, 60))
                if len(listcard) == 4:
                    screen.blit(
                        listcard[index], (rect.x-60+index*40+self.movecordinate[historyindex][0], rect.y+self.movecordinate[historyindex][1], 40, 60))
            historyindex += 1

    def place(self, listcard):
        activecard = []
        for card in listcard:
            if card.active:
                activecard.append(card)
        if self.value == 0:
            self.setcardhere(activecard)
            for card in activecard:
                listcard.remove(card)
        elif self.cardtype == "odd":
            if len(activecard) == 1:
                if activecard[0].value > self.value:
                    self.setcardhere(activecard)
                    for card in activecard:
                        listcard.remove(card)
            elif len(activecard) == 3:
                if activecard[-1].value*1000 > self.value:
                    self.setcardhere(activecard)
                    for card in activecard:
                        listcard.remove(card)
        elif self.cardtype == "even":
            if len(activecard) == 2:
                if activecard[0].value > self.value:
                    self.setcardhere(activecard)
                    for card in activecard:
                        listcard.remove(card)
            elif len(activecard) == 4:
                if activecard[-1].value*1000 > self.value:
                    self.setcardhere(activecard)
                    for card in activecard:
                        listcard.remove(card)

    def setcardhere(self, activecard):
        if len(activecard) == 1:
            self.val = activecard[0].val
            self.value = activecard[-1].value
            angletorotate = random.randint(-30, 30)
            img = [pygame.transform.rotate(pygame.transform.scale(
                pygame.image.load(f"photo/cardsprite/{activecard[0].name}"), (40, 60)), angletorotate)]
            self.keepcard.append(img)
            self.movecordinate.append(
                (random.randint(-10, 10), random.randint(-10, 10)))
        if len(activecard) == 2:
            self.val = activecard[0].val
            self.value = activecard[-1].value
            angletorotate = random.randint(-30, 30)
            img = [pygame.transform.rotate(pygame.transform.scale(
                pygame.image.load(f"photo/cardsprite/{activecard[i].name}"), (40, 60)), angletorotate) for i in range(2)]
            self.keepcard.append(img)
            self.movecordinate.append(
                (random.randint(-10, 10), random.randint(-10, 10)))
        if len(activecard) == 3:
            self.val = activecard[0].val
            self.value = activecard[-1].value*1000
            angletorotate = random.randint(-30, 30)
            img = [pygame.transform.rotate(pygame.transform.scale(
                pygame.image.load(f"photo/cardsprite/{activecard[i].name}"), (40, 60)), angletorotate) for i in range(3)]
            self.keepcard.append(img)
            self.movecordinate.append(
                (random.randint(-10, 10), random.randint(-10, 10)))
        if len(activecard) == 4:
            self.val = activecard[0].val
            self.value = activecard[-1].value*1000
            angletorotate = random.randint(-30, 30)
            img = [pygame.transform.rotate(pygame.transform.scale(
                pygame.image.load(f"photo/cardsprite/{activecard[i].name}"), (40, 60)), angletorotate) for i in range(3)]
            self.keepcard.append(img)
            self.movecordinate.append(
                (random.randint(-10, 10), random.randint(-10, 10)))
        self.cardtype = "odd" if len(activecard) % 2 == 1 else "even"
