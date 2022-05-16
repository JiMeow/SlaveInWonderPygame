import pygame


# It's a class that represents a playing card.
class Card():
    def __init__(self, name):
        """
        It takes a string, splits it into two parts, and then assigns a value to the second part

        :param name: the name of the card
        """
        self.name = name
        self.flowers, self.val = name[:-4].split("-")
        if self.val == 'T':
            self.val = 10
        elif self.val == 'J':
            self.val = 11
        elif self.val == 'Q':
            self.val = 12
        elif self.val == 'K':
            self.val = 13
        elif self.val == '1':
            self.val = 14
        elif self.val == '2':
            self.val = 15
        else:
            self.val = int(self.val)
        self.active = False
        self.value = self.val+ord(self.flowers[0])/1000

    def draw(self, screen, x, y):
        """
        If the card is active, draw it with a y offset of -20. Otherwise, draw it with a y offset of 0.

        :param screen: the screen you want to draw the card on
        :param x: x position of the card
        :param y: y position of the card
        """
        img = pygame.transform.scale(
            pygame.image.load(f"photo/cardsprite/{self.name}"), (40, 60))
        # draw card if card active
        if self.active:
            screen.blit(img, (x, y-20))
        # draw card if card not active
        else:
            screen.blit(img, (x, y))

    def click(self):
        """
        If the button is active, it will become inactive, and if it is inactive, it will become active
        """
        self.active = not self.active

    # set for sort
    def __lt__(self, obj):
        if self.val < obj.val:
            return True
        elif self.val == obj.val:
            if self.flowers < obj.flowers:
                return True
            else:
                return False

    def __gt__(self, obj):
        if self.val > obj.val:
            return True
        elif self.val == obj.val:
            if self.flowers > obj.flowers:
                return True
            else:
                return False

    def __le__(self, obj):
        if self.val < obj.val:
            return True
        elif self.val == obj.val:
            if self.flowers <= obj.flowers:
                return True
            else:
                return False

    def __ge__(self, obj):
        if self.val > obj.val:
            return True
        elif self.val == obj.val:
            if self.flowers >= obj.flowers:
                return True
            else:
                return False

    def __eq__(self, obj):
        if self.val == obj.val and self.flowers == obj.flowers:
            return True
        return False
