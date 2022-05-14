import pygame


class Player:
    def __init__(self, id, color):
        self.id = id
        self.color = color
        self.name = f"player{id}"
        self.room = "0"

    def draw(self, screen, x, y):
        pygame.draw.rect(screen, self.color, (x, y, 20, 20))
