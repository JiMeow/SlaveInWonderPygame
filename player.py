import pygame


class Player:
    def __init__(self, id, color):
        self.id = id
        self.color = color
        self.name = f"player{id}"
        self.room = "0"
        self.width = 20
        self.high = 20
        self.card = []
        self.iscompleteturn = False

    def draw(self, screen, x, y):
        pygame.draw.rect(screen, self.color, (x, y, self.width, self.high))
        textname = pygame.font.Font(None, int(20)).render(
            f"{self.name}", True, "white")
        screen.blit(textname, textname.get_rect(
            center=(x+self.width//2, y+self.high*3//2)))
