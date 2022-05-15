import pygame


class Card():
    def __init__(self, name):
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

    def draw(self, screen, x, y):
        img = pygame.transform.scale(
            pygame.image.load(f"photo/cardsprite/{self.name}"), (40, 60))
        screen.blit(img, (x, y))

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
